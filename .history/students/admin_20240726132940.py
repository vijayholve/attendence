from django.contrib import admin
from .models import Student,Attendance ,CustomUser ,Teacher
# Register your models here.
admin.site.register(Student)
admin.site.register(CustomUser)
admin.site.register(Teacher)
admin.site.register(Attendance) 


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from base.forms import CustomUserCreationForm, CustomUserChangeForm
