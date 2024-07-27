from celery import shared_task
from .seed import student_to_send_mail,teaches_to_send_mail
import datetime
@shared_task(bind=True)
def send_mail_task(self,id,subject,mail_text):
    student_to_send_mail(id,subject,mail_text)
    times=datetime.datetime.now()
    current_time = times.strftime("%Y-%m-%d %H:%M:%S")
    return f"procced at {current_time} "

@shared_task(bind=True)
def send_mail_to_all_task_teacher(self,subject,mail_text):
    teaches_to_send_mail(subject,mail_text)
    return "done"

def send_mail_to_all_task_teacher(self,subject,msg):
    teaches_to_send_mail(subject,mal_text)
    return "done"