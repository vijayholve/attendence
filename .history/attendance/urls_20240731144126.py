from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('students.urls')), 
    path('assignement/',include('students.urls')),
    path('account/', include('base.urls')),
     
     
]

