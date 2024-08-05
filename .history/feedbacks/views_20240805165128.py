from django.shortcuts import render,redirect
from .forms import feedbackform 
from django.contrib.auth.decorators import login_required 
from 

# Create your views here.
@login_required(login_url="login-page")
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

@login_required(login_url="login-page")
def list_feedbacks(request):
    feedbacks=feedback.objects.filter(student=request.user)  # Get all feedbacks for the logged-in user
    content={'feedbacks':feedbacks}
    return render(request,"feedbacks\list_feedbacks.html",content)  # Render the template with the feedbacks list

