from django.contrib import admin
from . import models


# Register your models here.

admin.site.register(models.Painting)
admin.site.register(models.Likes)
admin.site.register(models.Dislikes)