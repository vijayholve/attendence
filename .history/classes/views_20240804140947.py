from django.shortcuts import render
from .forms import classesform
def create_classes(request):
    form=classesform()
    content={}
    return render(request,"classes/create_class.html", content)