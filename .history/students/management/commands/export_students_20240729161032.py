import pandas as pd
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from students.models import Student, Attendance

class Command(BaseCommand):
    help = 'Export attendance data to an Excel file'

    def handle(self, *args, **kwargs):
        try:
            end_date = datetime.now().date()
            start_date = end_date - timedelta(days=6)

            students = Student.objects.all()

            # Prepare the attendance data
            data = []
            dates = [start_date + timedelta(days=i) for i in range(7)]

            for student in students:
                row = {
                    'Student ID': student.roll_no,
                    'Name': student.name,
                }
                for date in dates:
                    attendance = Attendance.objects.filter(student=student, date=date).first()
                    row[date] = 'Present' if attendance and attendance.present == 'present' else 'Absent'
                data.append(row)

            # Create DataFrame
            df = pd.DataFrame(data)

            # Define the Excel file path
            file_path = rf'downloads/attendance_data.xlsx'

            # Export to Excel
            df.to_excel(file_path, index=False)

            self.stdout.write(self.style.SUCCESS(f'Successfully exported attendance data to {file_path}'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error exporting attendance data: {e}'))
