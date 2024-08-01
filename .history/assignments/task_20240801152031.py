from celery import shared_task


@shared_task(bind=True)
def send_mail_to_all_task_teacher(self,subject,mail_text):
    assignement_have_to_send_msg(id)
    return "done"