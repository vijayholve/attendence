from django.shortcuts import render
from . models import Student,Attendance
# Create your views here.
def home(request):
    students=Student.objects.all()
    context={"students":students}
    return render(request,"students/home.html")