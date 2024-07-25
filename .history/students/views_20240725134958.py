from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect 
from .models import Student, Attendance 
from django.contrib.auth.decorators import login_required 
from django.utils import timezone 
from django.template.defaulttags import register 
from .form import studuntform ,subjectform  ,CustomUserCreationForm ,TeacherForm,AdminForm
from django.db.models import Q  
from .seed import register_user_to_send_mail
@register.filter 
def get_item(dictionary, key): 
    return dictionary.get(key)
def send_emails_users(request):
    
    if request.method == "POST":
        register_user_to_send_mail() 
        return redirect('home') 
    return redirect('home')
def create_students(request):
    forms=studuntform()
    if request.method == "POST":
        forms=studuntform(request.POST )
        if forms.is_valid():
            forms.save() 
            return redirect('home')
    content={'forms':forms}
    return render(request,"students/create_student.html",content)
def create_subjescts(request):
    forms=subjectform() 
    if request.method == "POST":
        forms=subjectform(request.POST)
        if forms.is_valid():
            forms.save() 
            return redirect('home')
    content={'forms':forms}
    return render(request,"students/create_subjects.html",content)
    
def student_list(request): 
    students = Student.objects.all() 
    today = timezone.now().date() 
    student_attendance = [] 
    student_presenty={} 
    for student in students:
        attendance_exists = Attendance.objects.filter(Q(student=student) & Q(date=today)).exists()
        student_attendance.append((student, attendance_exists)) 
    content={'student_attendance': student_attendance,"today":today} 
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



def register_page(request):
    if request.method == 'POST':
        user_form = (request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user_type = user_form.cleaned_data.get('user_type')
            if user_type == 1:
                student_form = studuntform(request.POST)
                if student_form.is_valid():
                    student = student_form.save(commit=False)
                    student.user = user
                    student.save()
            elif user_type == 2:
                teacher_form = TeacherForm(request.POST)
                if teacher_form.is_valid():
                    teacher = teacher_form.save(commit=False)
                    teacher.user = user
                    teacher.save()
            elif user_type == 3:
                admin_form = AdminForm(request.POST)
                if admin_form.is_valid():
                    admin = admin_form.save(commit=False)
                    admin.user = user
                    admin.save()
            login(request, user)
            return redirect('home')
    else:
        user_form = cus()
        student_form = studuntform()
        teacher_form = TeacherForm()
        admin_form = AdminForm()
    return render(request, 'students/register.html', {
        'user_form': user_form,
        'student_form': student_form,
        'teacher_form': teacher_form,
        'admin_form': admin_form
    })
