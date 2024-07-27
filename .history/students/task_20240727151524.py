from celery import shared_task
from .seed import student_to_send_mail,teaches_to_send_mail
import datetime
@shared_task(bind=True)
def send_mail_task(self,email,fullname):
    student_to_send_mail([email],fullname)
    times=datetime.datetime.now()
    current_time = times.strftime("%Y-%m-%d %H:%M:%S")
    return f"procced at {current_time} "

@shared_task(bind=True)
def send_mail_to_all_task(self):
    teaches_to_send_mail()
    return "done"