from django.urls import path 
from . import views
urlpatterns = [
    pathg
    path('create-assignment/',views.assignemt_form,name="create-assignment"),
    path('home-assignemts/',views.assignement_home,name="home-assignemts"),
        path('download/<int:file_id>/', views.download_file, name='download_file'),

]