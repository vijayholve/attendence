from django.shortcuts import render
from .forms import AssignmentForm
def assignemt_form(request):
    form=AssignmentForm()
    if request.method == "POST":
        

