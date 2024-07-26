from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect 
from .models import Student, Attendance ,CustomUser ,Teacher ,hod
from django.contrib.auth.decorators import login_required 
from django.utils import timezone 
from django.template.defaulttags import register 
from base.forms import studuntform ,subjectform 
from django.db.models import Q  
from .seed import register_user_to_send_mail 
from django.contrib.auth.decorators import login_required

def get_item(dictionary, key): 
    return dictionary.get(key)
def send_emails_users(request):
    
    if request.method == "POST":
        register_user_to_send_mail() 
        return redirect('home') 
    return redirect('home')
# def create_students(request):
#     forms=studuntform()
#     if request.method == "POST":
#         forms=studuntform(request.POST )
#         if forms.is_valid():
#             forms.save() 
#             return redirect('home')
#     content={'forms':forms}
#     return render(request,"students/create_student.html",content)
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
        username = user.username
        user_type = user.user_type 
    teacher = Teacher.objects.all() 
    today = timezone.now().date() 
    student_attendance = [] 
    student_presenty={} 
    print(user_type)
    content={'student_attendance': student_attendance,"today":today ,'username':username ,
             'user_type':user_type} 
    return render(request, 'students/home.html', content) 
    
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



