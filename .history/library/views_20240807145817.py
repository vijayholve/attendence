from django.shortcuts import render
from students.models import Books
# Create your views here.

def library_home(request):
    books=Books