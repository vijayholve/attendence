from django.shortcuts import render ,redirect
from .forms import classesform
from django.contrib.messages import error
def create_classes(request):
    form=classesform()
    if request.method == "POST":
        form=classesform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error(request,"Information is incorect")
    content={"form":form    }
    return render(request,"classes/create_class.html", content)

def classes_list(requets)