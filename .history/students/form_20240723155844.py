from django.forms import ModelForm
from .models import Student ,Teacher ,Subject 

class subjectform(ModelForm):
    class Meta:
        fields=['name'] 
        model=Subject
class studuntform(ModelForm):
    class Meta:
        fields=['name','subject'] 
        model=Student 

