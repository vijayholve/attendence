from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home")
    path('mark/<int:student_id>/', views.mark_attendance, name='mark_attendance'),

]
