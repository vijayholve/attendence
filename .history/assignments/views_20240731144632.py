from django.shortcuts import render
from .forms import AssignmentForm
def assignemt_form(request):
    form=AssignmentForm()
    if request.method == "POST":
        form=AssignmentForm(request.POST)
        if for
