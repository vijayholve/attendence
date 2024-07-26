from django.forms import ModelForm
from .models import Student ,Teacher ,Subject  ,CustomUser ,admin
from django.contrib.auth.forms import UserCreationForm 

class CustomeUserForm(UserCreationForm):
    class Meta:
        model=CustomUser 
        fields=('username','email','user_type') 
class subjectform(ModelForm):
    class Meta:
        model=Subject 
        fields=['name'] 
class studuntform(ModelForm):
    class Meta:
        fields=['name','subject'] 
        model=Student 

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('contact',)

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ('contact',)