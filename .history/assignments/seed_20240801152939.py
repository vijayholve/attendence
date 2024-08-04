from django.core.mail import send_mail 
from django.contrib.auth.models import User
from students.models import Assignment ,ClassGroup ,Student
from django.conf import settings 

def students_to_send_mail(id):
    sender=settings.EMAIL_HOST_USER
    assignment=Assignment.objects.get(id=id)
    classgroup=ClassGroup.objects.get(id=assignment.classgroup.id)
    students=Student.objects.filter()
    arr=[] 
    for std in student:
        if receiver_email:=std.user.email is None :
            return 'user does not have email'
         
        try:
            # sleep(5)
            print(receiver_email ,"Wait")
            send_mail(subject,email_content,sender,[receiver_email])
            print(receiver_email,"Done")
        except Exception as e:
            print(e)    