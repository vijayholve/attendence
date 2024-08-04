from students.models import Test 
from django.forms import ModelForm

class AssignmentForm(ModelForm):
    
    class Meta:
        model=Test
        fields=[CustomUser
title
subject
test_date
conducted_by] 
    def __init__(self, *args, **kwargs):
        super(AssignmentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label