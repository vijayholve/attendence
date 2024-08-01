from django.shortcuts import render ,redirect
from .forms import AssignmentForm
from django.contrib.messages import error
def assignemt_form(request):
    form=AssignmentForm()
    if request.method == "POST":
        due_date=request.POST.get('due_date')
        form=AssignmentForm(request.POST,request.FILES)
        if form.is_valid():
            if due_date:
                form=form.save(commit=False)
                form.due_date=due_date 
            form.save()
            return redirect('home') 
        else:
            error(request, "Invalid assignment")
    return render(request,rf'assignements\create_assignment.html', {'form': form})
