from django.db import models
from traitlets import default

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=400)
    author_name = models.CharField(max_length=400)
    price = models.IntegerField(default = 350)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name