from django.shortcuts import render
from .forms import feedbackform
# Create your views here.
def create_feedback(request):
    forms=feedbackform() 
    if request.method == "POST":
        forms=feedbackform(request.POST)
        if forms.is_valid():
            forms.save() 
            return redirect('home')
    content={'forms':forms}
    return render(request,"students/create_subjects.html",content)



