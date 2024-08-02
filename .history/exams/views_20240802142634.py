from django.shortcuts import render
from .forms import ExamsForm
from students.models import Test
# Create your views here.
def create_exams(request):  
    form = ExamsForm()
    if request.method == "POST":
        form=ExamsForm(request.POST,request.FILES)
        if form.is_valid():
            exams=form.save(commit=False)
             
            exams.save()
            # send_mail_to_all_students_for_assignemt.delay(assign.id)  
            return redirect('home') 
        else:
            error(request, "Invalid assignment")
    return render(request,"exams/exam_form.html")