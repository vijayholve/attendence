from django.urls import path 
from . import views

urlpatterns = [
    path('book-data/',views.library_home,name="book-data"),
    path("dowload"),
]