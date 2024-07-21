
from django.contrib import admin
from django.urls import path ,include

rlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Add this line
]