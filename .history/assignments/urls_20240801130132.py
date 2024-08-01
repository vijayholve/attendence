from django.urls import path 
from . import views
urlpatterns = [
    path('create-assignment/',views.assignemt_form,name="create-assignment"),
    path('create-assignment/',views.assignemt_form,name="home-assignemts"),
]
