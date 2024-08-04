from django.urls import path
from . import views

urlpatterns = [
    path("create-classes",views.home,name="home"),
] 
