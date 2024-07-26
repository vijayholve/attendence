from django.urls import path
from . import views
urlpatterns = [
    path("",views.student_list,name="home"),
    path('mark/<int:student_id>/', views.mark_attendance, name='mark_attendance'),
path('apsent/<int:student_id>/', views.mark_apsent,name="apsent"),
path('create-subject/',views.create_subjescts,name="create-subject"),
path('teacher-data/',views.teacher_list,name="teacher-data"),
path(),
]

