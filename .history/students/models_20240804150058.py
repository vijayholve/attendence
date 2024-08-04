from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Group, Permission
from datetime import datetime,timedelta 
class Classes(models.Model):
    name=
class ClassGroup(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=10, choices=[('FY', 'First Year'), ('SY', 'Second Year'), ('TY', 'Third Year')])

    def __str__(self):
        return f"{self.name} - {self.year}"
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
    name = models.CharField(max_length=100)
    # code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Student(models.Model):
    roll_no=models.IntegerField(unique=True,null=True,blank=True)
    name = models.CharField(max_length=100) 
    user = models.OneToOneField(CustomUser, on_delete=models.SET_NULL,null=True,blank=True)
    contact = models.CharField(max_length=150,null=True ,blank=True ) 
    email=models.EmailField(null=True ,blank=True)
    subject=models.ManyToManyField(Subject) 
    profile=models.ImageField(upload_to='profile_images/', default=rf"/profile_images/default.jpeg",
                             null=True,blank=True) 
    classgroup=models.ForeignKey(ClassGroup,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return f"{self.id} is {self.name}"  
    def schedule_welcome_message(self):
        # Schedule the task to run 1 minute from now
        eta = datetime.now() + timedelta(minutes=1)
        # send_scheduled_message.apply_async((self.user.id, 'Welcome to our platform!'), eta=eta)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Schedule welcome message after the student is saved
        self.schedule_welcome_message()


    
class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100) 
    contact = models.CharField(max_length=15,null=True ,blank=True)     
    city=models.CharField(max_length=200 ,null=True ,blank=True)  
    subject=models.OneToOneField(Subject,on_delete=models.SET_NULL ,blank=True , null=True)
    class_teacher_of = models.OneToOneField('ClassGroup', on_delete=models.SET_NULL, null=True, blank=True, related_name='class_teacher')
    
    def __str__(self):
        return self.name 
    
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField() 
    present = models.BooleanField(default=False)
    subject=models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True ,blank=True ) 
    def __str__(self):
        return f"{self.student.name} - {self.date} - {'Present' if self.present else 'Absent'}"
class Assignment(models.Model):  
    title = models.CharField(max_length=255) 
    description = models.FileField('assignment_images/') 
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE) 
    assigned_date = models.DateField(auto_now_add=True) 
    due_date = models.DateField() 
    assigned_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)  
    classgroup=models.ForeignKey(ClassGroup,on_delete=models.SET_NULL, 
                                 null=True,blank=True) 

    def __str__(self):
        return self.title

class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    submitted_date = models.DateField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.assignment.title} - {self.student.name}"

class Test(models.Model):
    title = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assigned_date = models.DateField(auto_now_add=True ,null=True,blank=True) 
    test_date = models.DateTimeField()
    conducted_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classgroup=models.ForeignKey(ClassGroup,on_delete=models.SET_NULL, 
                                 null=True,blank=True)  
    def __str__(self):
        return self.title 
    
class TestResult(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.test.title} - {self.student.name}"
