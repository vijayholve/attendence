from django.forms import ModelForm
from students.models import Assignment 


class AssignmentForm(ModelForm):
    class Meta:
        model=ass

