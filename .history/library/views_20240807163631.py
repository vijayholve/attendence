from django.shortcuts import render ,get_object_or_404 ,redirect
from students.models import Books 
import os
# Create your views here.
from .forms import BooksForm
from django.http import FileResponse, Http404 ,HttpResponse 
def library_home(request):
    books=Books.objects.all()
    content={"books":books} 
    return render(request,"librarys/book_home.html",content)

def books_form(request):
    form=BooksForm() 
    # teacher=Teacher.objects.get(name="hod2")
    if request.method == "POST":
        form=BooksForm(request.POST,request.FILES)
        if form.is_valid():
            assign=form.save(commit=False)
            
            assign.save()
            return redirect('home') 
        else:
            error(request, "Invalid ")
    return render(request,rf'assignements\create_assignment.html', {'form': form})

def download_file(request, file_id):
    downloadable_file = get_object_or_404(Books, id=file_id) 
    file_path = downloadable_file.file.path  
    if os.path.exists(file_path): 
        with open(file_path, 'rb') as file: 
            response = HttpResponse(file.read(), content_type='application/octet-stream') 
            response['Content-Disposition'] = f'attachment; filename={os.path.basename(file_path)}'
            return response
    else:
        raise Http404("File not found")