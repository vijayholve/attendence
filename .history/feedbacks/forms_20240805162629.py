from django.forms import ModelForm
from students.models import Feedback
class feedbackform(ModelForm):
    class Meta:
        model=Feedback
        fields="__all__"
