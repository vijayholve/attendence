from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
    choices=(
        (1, 'student'),
        (2, 'teacher'),
        (3, 'admin'),
    )
    user_type=models.IntegerField(choices=choices)
class Subject(models.Model):
    name=models.CharField(max_length=200) 
    def __str__(self):
        return self.name 

class Student(models.Model):
    name = models.CharField(max_length=100) 
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15)
    subject=models.man(Subject,blank=True , null=True)

    def __str__(self):
        return f"{self.roll_no} is {self.name}" 
    
class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE) 
    name=models.CharField(max_length=100) 
    city=models.CharField(max_length=200 ,null=True ,blank=True)  
    subject=models.OneToOneField(Subject,on_delete=models.SET_NULL ,blank=True , null=True)
    def __str__(self):
        return self.name 
    
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField() 
    present = models.BooleanField(default=False)
    subject=models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True ,blank=True ) 
    def __str__(self):
        return f"{self.student.name} - {self.date} - {'Present' if self.present else 'Absent'}"
