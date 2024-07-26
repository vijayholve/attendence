from django.db import models
from django.contrib.auth.models import User



class CustomUser(AbstractUser):
    contact = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    
    USERNAME_FIELD = 'username'  # or 'email' if you prefer using email as the username
    REQUIRED_FIELDS = ['email', 'contact', 'name']

class admin(models.Model):
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
    contact = models.CharField(max_length=15,null=True ,blank=True) 
    subject=models.ManyToManyField(Subject) 

    def __str__(self):
        return f"{self.roll_no} is {self.name}" 
    
class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100) 
    contact = models.CharField(max_length=15,null=True ,blank=True) 
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