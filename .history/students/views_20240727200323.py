from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect 
from .models import Student, Attendance ,CustomUser ,Teacher ,hod
from django.contrib.auth.decorators import login_required 
from django.utils import timezone 
from django.template.defaulttags import register 
from base.forms import studuntform ,subjectform 
from django.db.models import Q  
from .seed import teaches_to_send_mail ,student_to_send_mail
from django.contrib.auth.decorators import login_required
# views.py
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Student
import os
from django.conf import settings
from .models import Student
from .task import send_mail_to_all_task ,send_mail_task
def download_id_card(request, student_id):
    student = Student.objects.get(pk=student_id)
    html_content = render_to_string('students/id_card.html', {'student': student})
    css_path = os.path.join(settings.BASE_DIR, 'static', 'students', 'id_card.css')
    with open(css_path, 'r') as css_file:
        css_content = css_file.read()
    
    # Inline the CSS content into the HTML content
    html_with_css = f"<style>{css_content}</style>{html_content}"
    
    # Create the HTTP response with the HTML content
    response = HttpResponse(html_with_css, content_type='text/html')
    response['Content-Disposition'] = f'attachment; filename="{student.name}_id_card.html"'
    return response
def get_item(dictionary, key): 
    return dictionary.get(key)

def attendance_data_students(request):
    
    attendance_date=Attendance.objects.values('date').distinct()
    date_list = [entry['date'] for entry in attendance_date]
    formatted_dates = [date.strftime('%Y-%m-%d') for date in date_list]
    for datevar in formatted_dates:
        students=Attendance.objects.filter(date=datevar)
        for student in students:
            print(student)  

def create_subjescts(request):
    forms=subjectform() 
    if request.method == "POST":
        forms=subjectform(request.POST)
        if forms.is_valid():
            forms.save() 
            return redirect('home')
    content={'forms':forms}
    return render(request,"students/create_subjects.html",content)
def teacher_list(request):
    user=request.user 
    username=user.username
    if isinstance(user, CustomUser):    
        customuser = user
        user_type = user.user_type 
    teachers = Teacher.objects.all() 
    today = timezone.now().date() 
    print(user_type,"username",customuser.username)
    content={"today":today ,'customuser':customuser ,
             'user_type':user_type, 'teachers':teachers} 
    return render(request, 'students/teacher_data.html', content)  
    
    
def send_mails_to_teachers(request): 
    subject=request.POST.get('subject')  
    mail_text=request.POST.get('content')  
    if request.method == 'POST': 
        send_mail_to_all_task.delay(subject,mail_text) 
        return redirect('home') 
    content={} 
    return render(request,"students/send_mail.html",content)

@login_required(login_url='login-page')
def student_list(request): 
    user=request.user 
    username=user.username 
    if isinstance(user, CustomUser):    
        username = user.username 
        user_type = user.user_type 
    students = Student.objects.all() 
    today = timezone.now().date() 
    student_attendance = [] 
    student_presenty={} 
    print(user_type)
    for student in students:
        attendance_exists = Attendance.objects.filter(Q(student=student) & Q(date=today)).exists()
        student_attendance.append((student, attendance_exists)) 
    content={'student_attendance': student_attendance,"today":today ,'username':username ,
             'user_type':user_type} 
    return render(request, 'students/home.html', content) 

def send_mails_to_students(request,id): 
    subject=request.POST.get('subject')  
    mail_text=request.POST.get('content')  
    if request.method == 'POST': 
        send_mail_task.delay(id,subject,mail_text) 
        
        return redirect('home') 
    content={} 
    return render(request,"students/send_mail.html",content)
def check_presenty(id): 
    today=timezone.now().date() 
    student=Student.objects.get(id=id) 
    attendance=Attendance.objects.get_or_create(student= student ,date=today)
    return attendance.present 

def mark_attendance(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    today = timezone.now().date()
    attendance, created = Attendance.objects.get_or_create(student=student, date=today)
    attendance.present = True
    attendance.save()  
    return redirect('home')

def mark_apsent(request, student_id):
    student=get_object_or_404(Student,id=student_id)
    today=timezone.now().date()
    attendance=Attendance.objects.get(student=student,date=today)
    attendance.present=False
    attendance.save()
    return redirect("home") 


def id_card(request,id):
    student=Student.objects.get(id=id) 
    content={'student':student}
    return render(request,'students/id_card.html',content)
