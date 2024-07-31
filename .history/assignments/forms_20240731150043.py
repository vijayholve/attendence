from django.forms import ModelForm
from students.models import Assignment 


class AssignmentForm(ModelForm):
    class Meta:
        model=Assignment
        fields=['title','description','due_date','assigned_by']
    def __init__(self, *args, **kwargs):
        super(\, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label

