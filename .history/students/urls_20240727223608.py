from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path("",views.student_list,name="home"),
    path('mark/<int:student_id>/', views.mark_attendance, name='mark_attendance'),
path('apsent/<int:student_id>/', views.mark_apsent,name="apsent"),
path('create-subject/',views.create_subjescts,name="create-subject"),
path('teacher-data/',views.teacher_list,name="teacher-data"),
path('send-mail-teaches/',views.send_mails_to_teachers,name="send-mail-teaches"),
path('send-mail-teaches.',views.send_mails_to_students,name=""),
path('id-card/<str:id>/',views.id_card,name="id-card"),
path('send-mail-student/<str:id>/',views.send_mails_to_students,name="send-mail-student"),
    path('download-id-card/<int:student_id>/', views.download_id_card, name='download_id_card'),
path('attendance-data/',views.attendance_data_students,name='attendance-data'),
]
if settings.DEBUG:  
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root =settings.MEDIA_ROOT)
