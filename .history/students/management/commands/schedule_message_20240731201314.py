from datetime import timedelta ,datetime
from typing import Any
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from students.task import *


class Command(BaseCommand):
    help='Succed the programd'
    def handle(self, *args, **kwargs):
        user_id=2
        message='user Schedule message '
        eta=datetime.
        


