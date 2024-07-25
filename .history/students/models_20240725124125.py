from django.db import models
from django.contrib.auth.models import User


class costomeuser(models.Model):
    choices=(
        
    )
class Subject(models.Model):
    name=models.CharField(max_length=200) 
    def __str__(self):
        return self.name 

class Student(models.Model):
    name = models.CharField(max_length=100) 
    subject=models.ManyToManyField(Subject )
    def __str__(self):
        return self.name 
    
class Teacher(models.Model):
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
