from .models import Student,Attendance
from faker import Faker # type: ignore 
from django.core.mail import send_mail
def fakestudents(count):
    fake=Faker()
    for _ in range(0,count):
        studets=Student.objects.create(
            name=fake.name()
        )
        studets.save()
def register_user_to_send_mail(receiver_email,fullname):
    # hotel_obj=hotel.objects.get(id=3)
    hotel_name="vj Hotels"
    subject=f"Welcome to {hotel_name} – Your Account is Ready!"
    email_content = f"""
Subject: Welcome to {hotel_name} – Your Account is Ready!

Dear {fullname},

Thank you for creating an account with {hotel_name}! We're thrilled to have you join our community.

Explore our website to discover a variety of delicious dishes crafted by our expert chefs. Whether you crave savory, sweet, or anything in between, we have something to satisfy every palate.

Visit us at #Vj_hotel.com and start your culinary adventure today!

Bon appétit!

Best regards,
Vijay Gholve
{hotel_name} Team
"""   
    sender=settings.EMAIL_HOST_USER
    try:
        send_mail(subject,email_content,sender,receiver_email)
    except Exception as e:
        # message.error)
        print(e) 
    
    
