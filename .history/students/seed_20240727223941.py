from .models import Student,Attendance
from faker import Faker # type: ignore 
from django.core.mail import send_mail 
from django.contrib.auth.models import User
from .models import Teacher ,CustomUser ,Student 
from django.conf import settings 
from time import sleep
def fakestudents(count):
    fake=Faker()
    for _ in range(0,count):
        studets=Student.objects.create(
            name=fake.name()
        )
        studets.save()
        
def teaches_to_send_mail(subject,email_content):
    sender=settings.EMAIL_HOST_USER
    teachers=Teacher.objects.all()
    arr=[] 
    for teacher in teachers:
        receiver_email=teacher.user.email 
        try:
            # sleep(5)
            print(receiver_email ,"Wait")
            send_mail(subject,email_content,sender,[receiver_email])
            print(receiver_email,"Done")
        except Exception as e:
            print(e) 
            
def student_to_send_mail(id,subject,email_content):
    sender=settings.EMAIL_HOST_USER
    student=Student.objects.get(id=id)
    receiver_email=student.user.email
    try:
        # sleep(5)
        print(receiver_email ,"Wait")
        send_mail(subject,email_content,sender,[receiver_email])
        print(receiver_email,"Done")
    except Exception as e:
        print(e) 
    

def students_to_send_mail(subject,email_content):
    sender=settings.EMAIL_HOST_USER
    teachers=Student.objects.all()
    arr=[] 
    for teacher in teachers:
        receiver_email=teacher.user.email 
        try:
            # sleep(5)
            print(receiver_email ,"Wait")
            send_mail(subject,email_content,sender,[receiver_email])
            print(receiver_email,"Done")
        except Exception as e:
            print(e)     
def faker_students(lenth):
    fake=Faker()
    
    for i in range(lenth):
        user=CustomUser.objects.create(
        username=fake.name(),
        email=fake.email(),
            password=fake.password(length=10),
            user_type=1,
        )
        
        Student.objects.create(
    user=user,
        name=fake.name(),
        contact=fake.phone_number(),
        
           profile=fake.image_url()
        )
            
            
        
    