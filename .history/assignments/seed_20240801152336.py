

def students_to_send_mail(subject,email_content):
    sender=settings.EMAIL_HOST_USER
    student=Student.objects.all()
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