from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 
class subject(models.Model):
    name=models.CharField(200) 
    def __str__(self):
        return self.name 
class Teacher(models.Model):
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=200 ,null=True ,blank=True) 
    
    def __str__(self):
        return self.name 
    
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)
    teacher=models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True ,blank=True)
    def __str__(self):
        return f"{self.student.name} - {self.date} - {'Present' if self.present else 'Absent'}"
