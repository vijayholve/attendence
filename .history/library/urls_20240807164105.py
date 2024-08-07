from django.urls import path 
from . import views

urlpatterns = [
    path('book-data/',views.library_home,name="book-data"),
    path("create-book",views.library_home,name="create-book"),
    path("dowload-book/",views.download_file,name="dowload-book"),
]