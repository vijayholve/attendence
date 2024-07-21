from .models import Student,Attendance
from faker import Faker # type: ignore
def fakestudents(count):
    fake=Faker()
    for _ in count
    studets=Student.objects.create(
        name=fake.name()
    )
    
    
    
