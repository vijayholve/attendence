from .models import Student,Attendance
from faker import Faker # type: ignore 
from django.core.mail import send_mail 
from django.contrib.auth.models import User
from django.conf import settings
def fakestudents(count):
    fake=Faker()
    for _ in range(0,count):
        studets=Student.objects.create(
            name=fake.name()
        )
        studets.save()
def register_user_to_send_mail():
    # hotel_obj=hotel.objects.get(id=3)
    
    subject=f"Your Account is Ready!"
    email_content = f"""
    helllo users 
"""   
    sender=settings.EMAIL_HOST_USER
    users=User.objects.all() 
    for user in users:
        receiver_email=user.emai
        try:
            send_mail(subject,email_content,sender,receiver_email)
        except Exception as e:
            # message.error)
            print(e) 
        
    
