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
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import os
from .models import Student
import os
from django.conf import settings
from .models import Student

from django.shortcuts import render
from .models import Attendance, Student
from datetime import datetime, timedelta
from .task import send_mail_to_all_task_teacher ,send_mail_task , send_mail_to_all_task_students
from django import template



def download_id_card(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    html_content = render_to_string('students/id_card.html', {'student': student})
    css_path = os.path.join(settings.BASE_DIR, 'static', 'students', 'id_card.css')
    
    with open(css_path, 'r') as css_file:
        css_content = css_file.read()
    
    # Inline the CSS content into the HTML content
    html_with_css = f"<style>{css_content}</style>{html_content}"
    
    # Add image handling
    if student.profile and student.profile.url.startswith('http'):
        student_image_url = student.profile.url  # External URL
    else:
        student_image_url = request.build_absolute_uri(student.profile.url) if student.profile else ''
    
    html_with_css = html_with_css.replace('{{ student_image }}', student_image_url)
    
    # Create the HTTP response with the HTML content
    response = HttpResponse(html_with_css, content_type='text/html')
    response['Content-Disposition'] = f'attachment; filename="{student.name}_id_card.html"'
    return response

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key): 
    return dictionary.get(key)
def home(request):
    return render(request,"students/home.html")
def attendance_data_students(request):
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=6)  

    students = Student.objects.all()

    # Prepare the attendance data in a nested dictionary: {student_id: {date: status}}
    attendance_data = {
        student.id: {
            date: Attendance.objects.filter(student=student, date=date)
            for date in (start_date + timedelta(days=i) for i in range(7))
        }
        for student in students
    }

    # Generate the list of dates for the header
    dates = [start_date + timedelta(days=i) for i in range(7)]

    context = {
        'students': students,
        'attendance_data': attendance_data,
        'dates': dates,
    }
    return render(request, 'students/attendance_table.html', context)


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
        send_mail_to_all_task_teacher.delay(subject,mail_text) 
        return redirect('home') 
    content={} 
    return render(request,"base/send_mail.html",content)

@login_required(login_url='login-page')
def student_list(request): 
    user=request.user 
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
    return render(request,"base/send_mail.html",content) 

def send_mails_to_all_students(request): 
    subject=request.POST.get('subject')  
    mail_text=request.POST.get('content')  
    if request.method == 'POST': 
        send_mail_to_all_task_students.delay(subject,mail_text) 
        return redirect('home') 
    content={} 
    return render(request,"base/send_mail.html",content)
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
