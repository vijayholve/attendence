from django.shortcuts import render
from .forms import classesform
def create_classes(request):
    form=classesform()
    if request.method == "POST":
        for
    content={}
    return render(request,"classes/create_class.html", content)