import pandas as pd
from django.core.management.base import BaseCommand
from students.models import Student

class Command(BaseCommand):
    help = 'Export students data to an Excel file'

    def handle(self, *args, **kwargs):
        try:
            students = Student.objects.all()

            # Prepare data for DataFrame
            data = []
            for student in students:
                data.append({
                    'roll_no': student.roll_no,
                    'name': student.name,
                    'contact': student.contact,
                })

            # Create DataFrame
            df = pd.DataFrame(data)

            # Define the Excel file path
            file_path = 'studentsstudents_data.xlsx'

            # Export to Excel
            df.to_excel(file_path, index=False)

            self.stdout.write(self.style.SUCCESS(f'Successfully exported student data to {file_path}'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error exporting student data: {e}'))
