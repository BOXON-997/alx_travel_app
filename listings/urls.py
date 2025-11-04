from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.indexq, name='index'),
]

