from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Attendance
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def student_list(request):
    students = Student.objects.all()
    today = timezone.now().date()
    student_attendance = [] 
    student_presenty={} 
    today=timezone.now().date()
    conetent={'student_attendance': student_attendance ,"today":today}
    return render(request, 'students/home.html', conetent)


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
