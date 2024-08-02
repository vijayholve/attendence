from django.urls import path
from . import views


urlpatterns = [
    path('exam-create/',views.create_exams,name='exam-create'),
    path('exam-home/')




