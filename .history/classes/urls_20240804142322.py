from django.urls import path
from . import views

urlpatterns = [
    path("create-classes/",views.create_classes,name="create-classes"),
        path("create-classes/",views.create_classes,name="all-classes"),

] 
