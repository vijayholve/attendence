from django.contrib import admin
from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

data=[Student,
      Teacher,
      Attendance,
      hod,
    ClassGroup,
    Assignment ,
    Feedback
]

for model in data:
    admin.site.register(model)
