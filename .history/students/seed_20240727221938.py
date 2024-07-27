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
        
 def test_student_creation_with_long_password(self):
        # Create a user with a long password
        long_password = fake.password(length=15)
        user = CustomUser.objects.create(
            username=self.fake.name(),
            email=self.fake.email(),
            password=long_password,
            user_type='student'
        )

        # Try to create a student with the created user
        student = Student.objects.create(
            user=user,
            name=self.fake.name(),
            contact=self.fake.phone_number(),
            profile=self.fake.image_url()
        )
        
    