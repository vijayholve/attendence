from django.shortcuts import render,redirect
from .forms import feedbackform 
# Create your views here.
def create_feedback(request):
    forms=feedbackform() 
    user=request.user
    if request.method == "POST": 
        forms=feedbackform(request.POST) 
        if forms.is_valid(): 
            form=forms.save(commit=False)  
            form=
            return redirect('home') 
    content={'forms':forms} 
    return render(request,"feedbacks\create_feedback.html",content) 



