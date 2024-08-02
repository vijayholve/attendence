from students.models import Test 
from django.forms import ModelForm

class ExamsForm(ModelForm):
    
    class Meta:
        model=Test