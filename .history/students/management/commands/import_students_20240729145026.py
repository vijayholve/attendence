import pandas as pd
from django.core.management.base import BaseCommand
from students.models import Student
from faker import Faker
class Command(BaseCommand):
    help = 'Import students from an Excel file'

    def handle(self, *args, **kwargs):
        
        file_path = 'path_to_your_excel_file.xlsx'
        try:
            df = pd.read_excel(file_path)

            for _, row in df.iterrows():
                Student.objects.create(
                    roll_no=row['roll_no'],
                    name=row['name'],
                    contact=row.get('contact', None)
                )
                
            self.stdout.write(self.style.SUCCESS('Successfully imported student data'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error importing student data: {e}'))
