import pandas as pd
from django.core.management.base import BaseCommand
from students.models import Student, Subject
from attendance.models import CustomUser

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
                user, created = CustomUser.objects.get_or_create(username=row['username'])
                
                # Create the student object
                student = Student.objects.create(
                    roll_no=row['roll_no'],
                    name=row['name'],
                    user=user,
                    contact=row['contact'],
                )

                # Associate subjects with the student
                subject_names = row['subjects'].split(',')  # Assuming subjects are comma-separated
                for subject_name in subject_names:
                    subject, _ = Subject.objects.get_or_create(name=subject_name.strip())
                    student.subject.add(subject)

                student.save()

            self.stdout.write(self.style.SUCCESS('Successfully imported student data'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error importing student data: {e}'))
