from django.shortcuts import render ,redirect
from .forms import AssignmentForm
from django.contrib.messages import error
def assignemt_form(request):
    form=AssignmentForm()
    if request.method == "POST":
        form=AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
        else:
            error(request, "Invalid assignment")
    return render(request,'C:\Users\Vijay\python pro\attendance\templates\assignements\create_assignment.html', {'form': form})

