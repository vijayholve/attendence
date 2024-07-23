from django.forms import ModelForm

class studuntform(ModelForm):
    class Meta:
        field=['name',]

