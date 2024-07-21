from django.shortcuts import render
from . models import Student,Attendance
# Create your views here.
def home(request):
    students=Student.objects.all()
    context={"students":students}
    return render(request,"students/home.html",context)

@login_required
def mark_attendance(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    attendance, created = Attendance.objects.get_or_create(student=student, date=timezone.now().date())
    attendance.present = True
    attendance.save()
    return redirect('attendance:student_list')