from datetime import date
from students.models import Test 
from django.forms import ModelForm
# forms.py
from django import forms
from django.forms import ModelForm

class ExamsForm(ModelForm):
    class Meta:
        model = Test
        fields = ['title', 'subject', 'conducted_by','classgroup']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Correctly call the parent class's __init__ method
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        test_date = cleaned_data.get('test_date')
        conducted_by = cleaned_data.get('conducted_by')

        # Example condition: Ensure the test date is in the future
        if test_date and test_date < date.today():
            self.add_error('test_date', 'Test date must be in the future.')

        # Example condition: Ensure title is not empty
        if not title:
            self.add_error('title', 'Title is required.')

        # Add any other condition
        if title and 'exam' not in title.lower():
            self.add_error('title', 'Title must contain the word "exam".')

        return cleaned_data