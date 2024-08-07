from django.forms import ModelForm
from students.models import Assignment 
from datetime import datetime, date
from django import forms
from django.forms import ModelForm ,DateInput


class AssignmentForm(ModelForm):
    
    class Meta:
        model=Assignment
        fields=['title','description','subject','due_date','classgroup','assigned_by']  
        widgets = {
            'due_date': DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Correctly call the parent class's __init__ method
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        test_date = cleaned_data.get('test_date')

        if test_date and test_date < date.today():
            self.add_error('due_date', 'Test date must be in the future.')

        if not title:
            self.add_error('title', 'Title is required.')