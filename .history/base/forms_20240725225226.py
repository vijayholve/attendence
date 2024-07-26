from django.forms import ModelForm
from students.models import Student ,Teacher ,Subject  ,CustomUser ,admin
from django.contrib.auth.forms import UserCreationForm 
from django import forms

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1',  'user_type')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_type'].widget = forms.RadioSelect(choices=CustomUser.USER_TYPE_CHOICES)

class subjectform(ModelForm):
    class Meta:
        model=Subject 
        fields=['name']     
class studuntform(ModelForm):
    class Meta:
        model=Student 
        fields=['name','subject','contact'] 

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ('name','contact')

class AdminForm(ModelForm):
    class Meta:
        model = admin
        fields = ('contact','name')  