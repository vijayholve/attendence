from datetime import datetime, date
from students.models import Test 
from django import forms
from django.forms import ModelForm ,DateInput

class ExamsForm(ModelForm):
    class Meta:
        model = Test
        fields = ['title', 'subject', 'conducted_by','classgroup','test_date']
        widgets = {
            'test_date': DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Correctly call the parent class's __init__ method
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        test_date = cleaned_data.get('test_date')
        conducted_by = cleaned_data.get('conducted_by')

        if test_date and test_date < date.today():
            self.add_error('test_date', 'Test date must be in the future.')

        if not title:
            self.add_error('title', 'Title is required.')

        # if title and 'exam' not in title.lower():
        #     self.add_error('title', 'Title must contain the word "exam".')

        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data.get('title')
        # if not title:
        #     raise forms.ValidationError('Title is required.')
        # if 'exam' or 'test'  not in title.lower():
        #     raise forms.ValidationError('Title must contain the word "exam".')
        return title

    def clean_test_date(self):
        test_date = self.cleaned_data.get('test_date')
        if test_date:
            # Convert test_date to a datetime.date object if it is a datetime.datetime object
            if isinstance(test_date, datetime):
                test_date = test_date.date()
            if test_date < date.today():
                raise forms.ValidationError('Test date must be in the future.')
        return test_date 