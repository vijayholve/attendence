from django.shortcuts import render ,redirect
from .forms import AssignmentForm
from django.contrib.messages import error
def assignemt_form(request):
    form=AssignmentForm()
    if request.method == "POST":
        date=request.POST.get('date_')
        form=AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            form.dur_date=""
            return redirect('home') 
        else:
            error(request, "Invalid assignment")
    return render(request,rf'assignements\create_assignment.html', {'form': form})

