from django.db import models
from django.contrib.auth.models import user
# Create your models here.
class students(models.Model):
    
    name=models.CharField(max_length = 100)
    