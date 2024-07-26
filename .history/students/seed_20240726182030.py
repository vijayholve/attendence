from .models import Student,Attendance
from faker import Faker # type: ignore 
from django.core.mail import send_mail 
from django.contrib.auth.models import User
from .models import Teacher
from django.conf import settings 
from time import sleep
def fakestudents(count):
    fake=Faker()
    for _ in range(0,count):
        studets=Student.objects.create(
            name=fake.name()
        )
        studets.save()
def register_user_to_send_mail():
    subject = "Your Account is Ready!"
    email_content = """
    helllo users 
"""
    sender=settings.EMAIL_HOST_USER
    teachers=Teacher.objects.all()
    arr=[] 
    for teacher in teachers:
        receiver_email=teacher. 
        try:
            # sleep(5)
            print(receiver_email ,"Wait")
            send_mail(subject,email_content,sender,[receiver_email])
            print(receiver_email,"Done")
        except Exception as e:
            print(e) 