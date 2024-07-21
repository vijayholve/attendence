from .models import Student,Attendance
from faker import Faker # type: ignore
def fakestudents(count):
    fake=Faker()
    for _ in range(0,count):
        studets=Student.objects.create(
            name=fake.name()
        )
        studets.save()
    
    
    
