from django.forms import ModelForm
from .models import Student ,Teacher ,Subject 
from django.contrib.auth.forms import UserCreationForm 
from django.forms import ModelForm 
from students.models import CustomUser  


class subjectform(ModelForm):
    class Meta:
        fields=['name'] 
        model=Subject 
class studuntform(ModelForm):
    class Meta:
        fields=['name','subject'] 
        model=Student 

