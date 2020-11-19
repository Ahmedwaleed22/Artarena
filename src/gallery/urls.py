from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery.as_view(), name='gallery'),
    path('add/', views.add.as_view(), name='add'),
]