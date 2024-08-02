from django.shortcuts import render
from .forms import *
# Create your views here.
def create_exams(request):  
    form = ExamForm()
    return render(request,"exams/exam_form.html")