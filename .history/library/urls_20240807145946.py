from django.urls import path 
from . import views

urlpatterns = [
    path('book-home/',views.library_home,name=""),
]