from django.shortcuts import render
from . models import Student
# Create your views here.
def home(request):
    students=
    return render(request,"students/home.html")