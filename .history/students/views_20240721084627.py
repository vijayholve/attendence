from django.shortcuts import render
from . models import Student,Attendance
# Create your views here.
def home(request):
    students=students.objects.all()
    return render(request,"students/home.html")