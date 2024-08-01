from django.shortcuts import render ,redirect
from .forms import AssignmentForm
from django.contrib.messages import error
from students.models import Teacher ,CustomUser
def assignemt_form(request):
    form=AssignmentForm() 
    teacher=Teacher     .objects.get(name="hod2")
    if request.method == "POST":
        due_date=request.POST.get('due_date')
        form=AssignmentForm(request.POST,request.FILES)
        if form.is_valid():
            assign=form.save(commit=False)
            if due_date:
                assign.due_date=due_date 
            assign.assigned_by=teacher
            assign.save()
            return redirect('home') 
        else:
            error(request, "Invalid assignment")
    return render(request,rf'assignements\create_assignment.html', {'form': form})

