from django.forms import ModelForm
from students.models import Student, Teacher ,

class classesform(ModelForm):
    class Meta:
        fields=[]