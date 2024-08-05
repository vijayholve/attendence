from django.shortcuts import render,redirect
from .forms import feedbackform 
# Create your views here.
from django.contrib.auth.decorators import login_required

def create_feedback(request):
    forms=feedbackform() 
    
    if request.method == "POST":  
        forms=feedbackform(request.POST) 
        if forms.is_valid():  
            feedback = forms.save(commit=False)
            feedback.student = request.user  # Set the student field to the logged-in user
            feedback.save()
            return redirect('home') 
    content={'forms':forms} 
    return render(request,"feedbacks\create_feedback.html",content) 



