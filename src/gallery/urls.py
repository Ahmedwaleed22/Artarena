from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery.as_view(), name='gallery'),
]