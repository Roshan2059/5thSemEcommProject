from django.shortcuts import render
from django.views.generic import View
from .models import *


# Create your views here.
def productView(request):
    products = Product.objects.all()
    context = { 
        'products' : products
    }
    return render(request, 'index.html', context)
