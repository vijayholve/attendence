from django.urls import path
from . import views

urlpatterns = [
path('create-feedback/',views.create_feedback,name="create-feedback"),

]
