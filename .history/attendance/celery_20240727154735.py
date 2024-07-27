from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance.settings')

app = Celery('attendance')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')
app.config_from_object(settings, namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-meail-every-day-at-8': {
        'task': 'base.tasks.send_mail_booking_task',
        'schedule': crontab(hour=14, minute=20),
    }
}

@app.task(bind=True)
def bind_fun(self):
    print(f"Request: {self.request!r}")
