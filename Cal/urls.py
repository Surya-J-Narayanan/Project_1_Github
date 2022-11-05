from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.cal, name='cal'),
    path('google',views.google, name='google'),
    path('add', views.add, name='add')
    
]