from django.db import models
import os
from django.conf import settings
from django.contrib.auth.models import User

from .author import Author
from .category import Category


def images_path():
    return os.path.join(settings.BASE_DIR, 'images')


def no_image_path():
    return os.path.join(settings.BASE_DIR, 'images/no-image.png')


class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    owned_by = models.ManyToManyField(User, through='UserBook')
    image = models.ImageField(upload_to=images_path, default=no_image_path)
    category = models.ForeignKey(Category.name, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
