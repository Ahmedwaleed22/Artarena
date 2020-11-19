from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    random_number = User.objects.make_random_password(length=10, allowed_chars='1234567890')
    EditedFileName = "%s.%s" % (random_number + '_' + filename, '')
    return os.path.join('paintings', EditedFileName)


class Painting(models.Model):
    Painting = models.ImageField(upload_to=get_file_path)
    PaintingName = models.CharField(max_length=255)
    PaintingDesc = models.TextField()
    PaintingCat = models.CharField(max_length=255)
    Artist = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.PaintingName