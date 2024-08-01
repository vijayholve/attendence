from django.forms import ModelForm
from students.models import Assignment 


class AssignmentForm(ModelForm):
    
    class Meta:
        model=Assignment
        fields=['title','description','subject',] 
    def __init__(self, *args, **kwargs):
        super(AssignmentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label

