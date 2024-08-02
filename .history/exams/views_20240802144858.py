from django.shortcuts import render, redirect 
from .forms import ExamsForm
from students.models import Test 
from django.contrib.messages import error

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
    content={"form":form}
    return render(request,"exams/exam_form.html",content)


def assignement_home(request):
    Test=Test.objects.all()
    content={'assignments': tests}
    return render(request,rf'assignements\assignemts_home.html',content)