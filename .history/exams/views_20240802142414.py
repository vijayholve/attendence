from django.shortcuts import render
from .forms import ExamsForm
# Create your views here.
def create_exams(request):  
    form = ExamsForm()
    return render(request,"exams/exam_form.html")