from django.shortcuts import render,redirect
from .forms import feedbackform 
# Create your views here.
def create_feedback(request):
    forms=feedbackform() 
    
    if request.method == "POST": 
        forms=feedbackform(request.POST) 
        if forms.is_valid(): 
            forms=forms.save(commit=False)  
            forms.student =request.user
            forms.save()
            return redirect('home') 
    content={'forms':forms} 
    return render(request,"feedbacks\create_feedback.html",content) 



