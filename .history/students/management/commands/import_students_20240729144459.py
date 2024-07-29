import pandas as pd
from django.core.management.base import BaseCommand
from students.models import Student, Subject ,CustomUser
from faker import Faker
class Command(BaseCommand):
    help = 'Import student data from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the Excel file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            # Read the Excel file
            df = pd.read_excel(file_path)

            # Iterate over the rows in the DataFrame and create Student objects
            for index, row in df.iterrows():
                # Retrieve or create the associated CustomUser object
                fake=Faker()

                # Create the student object
                student = Student.objects.create(
                    rollno=row['roll_no'],
                    name=row['name'],
                    email=fake.email(),
                    contact=fake.phone_number(),
                )

                student.save()

            self.stdout.write(self.style.SUCCESS('Successfully imported student data'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error importing student data: {e}'))
