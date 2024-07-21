from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Attendance
from django.contrib.auth.decorators import login_required
from django.utils import timezone


def student_list(request):
    students = Student.objects.all()
    today = timezone.now().date()
    student_attendance = [] 
    student_present
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
    return redirect('students:home')
