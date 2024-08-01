from celery import shared_task


@shared_task(bind=True)
def send_mail_to_all_task_teacher(self,subject,mail_text):
    teaches_to_send_mail(subject,mail_text)
    return "done"