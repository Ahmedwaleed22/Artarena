from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import Http404
from .models import Painting

# Create your views here.

class gallery(View):
    def get(self, request):
        Paintings = Painting.objects.all()
        return render(request, 'gallery.html', {'paintings': Paintings})


class add(View):
    template = 'addphoto.html'
    def post(self, request):
        painting = request.FILES["file"]
        paintingname = request.POST.get("name")
        paintingdesc = request.POST.get("description")
        paintingcategory = request.POST.get("category")

        if painting != "" and paintingname != "" and paintingdesc != "" and paintingcategory != None:
            addpainting = Painting(Painting=painting, PaintingName=paintingname,
            PaintingDesc=paintingdesc, PaintingCat=paintingcategory, Artist=request.user)
            addpainting.save()
            
            return render(request, self.template, {"MSG": "Your Brand New Painting Successfully Added"})

        else:
            return render(request, self.template, {"MSG": "Please Check That All Fields Are Not Empty"})


    def get(self, request):
        if not request.user.is_authenticated:
            raise Http404
        return render(request, self.template, {})


class PaintingView(View):
    def get(self, request, name, id):
        painting = get_object_or_404(Painting, id=id)

        if name == painting.PaintingName:
            return render(request, 'Painting.html', {"painting": painting})

        else:
            raise Http404