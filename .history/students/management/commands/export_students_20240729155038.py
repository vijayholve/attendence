import pandas as pd
from django.core.management.base import BaseCommand
from students.models import Student

class Command(BaseCommand):
    help = 'Export students data to an Excel file'

    def handle(self, *args, **kwargs):
        v
        try:
            students = Student.objects.all()

            # Prepare data for DataFrame
            data = []
            for student in students:
                data.append(attendance_data = {
        student.id: {
            date: Attendance.objects.filter(student=student, date=date)
            for date in (start_date + timedelta(days=i) for i in range(7))
        }
        for student in students
    }
)

            # Create DataFrame
            df = pd.DataFrame(data)

            # Define the Excel file path
            file_path = rf"C:\Users\Vijay\Downloads\students_data.xlsx"

            df.to_excel(file_path, index=False)

            self.stdout.write(self.style.SUCCESS(f'Successfully exported student data to {file_path}'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error exporting student data: {e}'))