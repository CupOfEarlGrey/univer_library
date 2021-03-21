from os import path
from uuid import uuid4
from django.db import models


# Create your models here.
def get_file_name(filename):
    ext = filename.strip().split('.')[-1]
    filename = f"{uuid4()}.{ext}"
    return path.join("images", filename)


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)
    book_order = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.name}: {self.author}"
