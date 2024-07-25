from django.contrib.auth.forms import UserCreationForm class FormName(forms.ModelForm):
    class Meta:
        model = ModelName
        fields = [Model Fields]