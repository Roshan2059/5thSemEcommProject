from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=400)
    author_name = models.CharField(max_length=400)
    isbn = models.IntegerField()
    price = models.IntegerField
    image = models.ImageField(upload_to='media/books')

    def __str__(self):
        return self.name