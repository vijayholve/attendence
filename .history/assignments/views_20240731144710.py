from django.shortcuts import render
from .forms import AssignmentForm
def assignemt_form(request):
    form=AssignmentForm()
    if request.method == "POST":
        form=AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return red
    return render(request,'assignment_form.html', {'form': form})

