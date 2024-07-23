from django.forms import ModelForm


class subjectform(ModelForm):
    class Meta:
        fields=[[name]]
class studuntform(ModelForm):
    class Meta:
        field=['name','']

