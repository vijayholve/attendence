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
    
    for student in students:
        attendance_exists = Attendance.objects.filter(student=student, date=today).exists()
        student_attendance.append((student, attendance_exists)) 
    return render(request, 'students/home.html', {'student_attendance': student_attendance})


def mark_attendance(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    today = timezone.now().date()
    attendance, created = Attendance.objects.get_or_create(student=student, date=today)
    attendance.present = True
    attendance.save()
    return redirect('home')

def mark_apsent(request, student_id):
    Student=get_object_or_404(id-s)
