from django.urls import path
from . import views
urlpatterns = [
    path("",views.all_api,name="all-api"),
    path("students/",views.studentAPI,name="students-api")
   
]
