from django.shortcuts import render
from .forms import classesform
def create_classes(request):
    form=classesform()
    if request.method == "POST":
        form=classesform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            
    content={}
    return render(request,"classes/create_class.html", content)