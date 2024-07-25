from django.contrib import admin
from .models import Student,Attendance ,CustomUser ,Teacher
# Register your models here.
admin.site.register(Student)

admin.site.register(Attendance)