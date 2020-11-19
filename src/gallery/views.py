from django.shortcuts import render
from django.views import View
from django.http import Http404

# Create your views here.

class gallery(View):
    def get(self, request):
        return render(request, 'gallery.html', {})


class add(View):
    def get(self, request):
        if not request.user.is_authenticated:
            raise Http404
        return render(request, 'addphoto.html', {})