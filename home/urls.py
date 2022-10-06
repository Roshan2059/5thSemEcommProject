from django.urls import path
from .views import *
from home import views

urlpatterns = [
    path('', views.productView, name='home'),
]