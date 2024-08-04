from django.shortcuts import render

def create_classes(request):
    
    content={}
    return render(request,"classes/create_class.html", content)