from django.urls import path
from .views import *
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
]