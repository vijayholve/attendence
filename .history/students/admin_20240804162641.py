from django.contrib import admin
from .models import Student,Attendance ,CustomUser ,Teacher ,hod ,Assignment
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Student)
admin.site.register(CustomUser,UserAdmin) 
admin.site.register(Teacher)
admin.site.register(Attendance) 
admin.site.register(hod)
admin.site.register(Assignment)

