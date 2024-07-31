from django.shortcuts import render ,redirect
from .forms import AssignmentForm
from django.contrib.
def assignemt_form(request):
    form=AssignmentForm()
    if request.method == "POST":
        form=AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
        else:
            
    return render(request,'assignment_form.html', {'form': form})

