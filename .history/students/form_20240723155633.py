from django.forms import ModelForm


class subjectform(ModelForm):
    class class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'
class studuntform(ModelForm):
    class Meta:
        field=['name','']

