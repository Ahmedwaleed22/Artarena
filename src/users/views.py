from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from django.views import View
from django.core.mail import send_mail
from gallery.models import Painting

# Create your views here.

class Login(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')

        return render(request, 'users/login.html', {'error': 'Please Check Your Email And Password'}) 


    def get(self, request):
        if request.user.is_authenticated:
            raise Http404
        return render(request, 'users/login.html', {})


class Register(View):
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username):
            return render(request, 'users/register.html', {'error': 'Username Is Already Taken'})

        elif User.objects.filter(email=email):
            return render(request, 'users/register.html', {'error': 'Email Is Already Taken'})

        else:
            user = User.objects.create_user(username, email, password)

            user.save()

            return redirect('/login')

        return render(request, 'users/register.html', {})


    def get(self, request):
        if request.user.is_authenticated:
            raise Http404

        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})


class Profile(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'profile.html', {})

        raise Http404


class PublicProfile(View):
    def get(self, request, user):
        if User.objects.filter(username=user).exists():
            fetchedUser = User.objects.get(username=user)
            paintings = Painting.objects.filter(Artist=fetchedUser)
            return render(request, 'publicProfile.html', {'fetchedUser': fetchedUser, 'paintings': paintings})

        raise Http404