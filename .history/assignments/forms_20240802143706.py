from django.forms import ModelForm
from students.models import Assignment 


class AssignmentForm(ModelForm):
    
    class Meta:
        model=Assignment
        fields=['title','description','subject','classgroup'] 
  # forms.py
from django import forms
from django.forms import ModelForm
from .models import Test

class ExamsForm(ModelForm):
    class Meta:
        model = Test
        fields = ['title', 'subject', 'test_date', 'conducted_by']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Correctly call the parent class's __init__ method
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label


