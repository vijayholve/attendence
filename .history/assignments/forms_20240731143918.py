from django.forms import ModelForm
from students.models import Assignment 


class AssignmentForm(ModelForm):
    class Meta:
        model=Assignment
        fields=['title','description','due_date','teacher']

