from django.shortcuts import render ,redirect ,get_object_or_404
from .forms import AssignmentForm
from django.contrib.messages import error
from students.models import Teacher ,CustomUser ,Assignment 
from django.http import FileResponse, Http404 ,HttpResponse
from .task import send_mail_to_all_students_for_assignemt
import os
def download_file(request, file_id):
    downloadable_file = get_object_or_404(Assignment, id=file_id)
    file_path = downloadable_file.description.path 
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename={os.path.basename(file_path)}'
            return response
    else:
        raise Http404("File not found")
def assignemt_form(request):
    form=AssignmentForm() 
    teacher=Teacher.objects.get(name="hod2")
    if request.method == "POST":
        due_date=request.POST.get('due_date')
        form=AssignmentForm(request.POST,request.FILES)
        if form.is_valid():
            assign=form.save(commit=False)
            if due_date:
                assign.due_date=due_date 
            assign.assigned_by=teacher 
            assign.save()
            send_mail_to_all_students_for_assignemt.delay(assign.id)  
            return redirect('home') 
        else:
            error(request, "Invalid assignment")
    return render(request,rf'assignements\create_assignment.html', {'form': form})

def assignement_home(request):
    assignments=Assignment.objects.all()
    content={'assignments': assignments}
    return render(request,rf'assignements\assignemts_home.html',content)
    