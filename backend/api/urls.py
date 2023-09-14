from django.urls import path
from . import views  #to grap ur view here

#from .views import api_home

urlpatterns = [
       path('' , views.api_home)  # lcoalhost:8000/api/ 
]

