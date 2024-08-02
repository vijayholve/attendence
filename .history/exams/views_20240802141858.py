from django.shortcuts import render

# Create your views here.
def create_exams(request):
    return render(request,"exams/exam_form.html")