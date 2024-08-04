from django.shortcuts import render, redirect 
from .forms import ExamsForm
from students.models import Test 
from django.contrib.messages import error

# Create your views here.
def create_exams(request):  
    form = ExamsForm()
    if request.method == "POST":
        form=ExamsForm(request.POST,request.FILES)
        due_date=request.POST.get('due_date')
        if form.is_valid():
            exams=form.save(commit=False)
            if due_date:
                exams.test=due_date 
            exams.save()
            # send_mail_to_all_students_for_assignemt.delay(assign.id)  
            return redirect('home') 
        else:
            error(request, "Invalid assignment")
    content={"form":form}
    return render(request,"exams/exam_form.html",content)


def home_exams(request):
    tests=Test.objects.all()
    content={'tests': tests}
    return render(request,rf'exams\tests_home.html',content)