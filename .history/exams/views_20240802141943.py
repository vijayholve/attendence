from django.shortcuts import render
from forms
# Create your views here.
def create_exams(request):  

    return render(request,"exams/exam_form.html")