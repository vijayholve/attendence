from django.contrib import admin
from .models import 
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Student)
admin.site.register(CustomUser,UserAdmin) 
admin.site.register(Teacher)
admin.site.register(Attendance) 
admin.site.register(hod)
admin.site.register(Assignment)

