from django.shortcuts import render
from .forms import ExamsForm
from students.models import 
# Create your views here.
def create_exams(request):  
    form = ExamsForm()
    teacher=Teacher.objects.get(name="hod2")
    if request.method == "POST":
        due_date=request.POST.get('due_date')
        form=AssignmentForm(request.POST,request.FILES)
        if form.is_valid():
            assign=form.save(commit=False)
            if due_date:
                assign.due_date=due_date 
            assign.assigned_by=teacher 
            assign.save()
            send_mail_to_all_students_for_assignemt.delay(assign.id)  
            return redirect('home') 
        else:
            error(request, "Invalid assignment")
    return render(request,"exams/exam_form.html")