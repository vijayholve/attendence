from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.shortcuts import render
from .models import Attendance, Student
from datetime import datetime, timedelta

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'student'),
        (2, 'teacher'),
        (3, 'Hod'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    groups = models.ManyToManyField(Group, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set')

class hod(models.Model):
    name=models.CharField(max_length=200)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)       
    contact = models.CharField(max_length=15,null=True ,blank=True) 


class Subject(models.Model):
    name=models.CharField(max_length=200) 
    def __str__(self):
        return self.name 

class Student(models.Model):
    name = models.CharField(max_length=100) 
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
    contact = models.CharField(max_length=15,null=True ,blank=True ) 
    subject=models.ManyToManyField(Subject) 
    profile=models.ImageField(upload_to='profile_images/', default=rf"/profile_images/default.jpeg",
                             null=True,blank=True)

    def __str__(self):
        return f"{self.id} is {self.name}" 
    
class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100) 
    contact = models.CharField(max_length=15,null=True ,blank=True) 
    city=models.CharField(max_length=200 ,null=True ,blank=True)  
    subject=models.OneToOneField(Subject,on_delete=models.SET_NULL ,blank=True , null=True)
    def __str__(self):
        return self.name 
    
def attendance_data_students(request):
    # Define the date range
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=3)  # Adjust the range as needed

    # Get all students
    students = Student.objects.all()

    # Prepare the attendance data
    attendance_data = {}
    for student in students:
        attendance_data[student] = Attendance.objects.filter(student=student, date__range=(start_date, end_date))

    # Generate the list of dates for the header
    dates = [start_date + timedelta(days=i) for i in range(4)]

    context = {
        'attendance_data': attendance_data,
        'dates': dates,
    }
    return render(request, 'students/attendance_table.html', context)
   
   
