from django.contrib import admin
from .models import Student,Attendance ,CustomUser ,Teacher ,admin
# Register your models here.
admin.site.register(Student)
admin.site.register(CustomUser)
admin.site.register(Teacher)
admin.site.register(Attendance) 
admin.site.register(admin) 


