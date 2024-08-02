from students.models import Test 
from django.forms import ModelForm

class ExamsForm(ModelForm):
    
    class Meta:
        model=Test
        fields=['title','subject','test_date','conducted_by'] 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Correctly call the parent class's __init__ method