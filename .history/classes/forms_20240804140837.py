from django.forms import ModelForm
from students.models import Student, Teacher ,ClassGroup

class classesform(ModelForm):
    class Meta:
        fields=[]