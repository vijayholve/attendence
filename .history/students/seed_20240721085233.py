from .models import Student,Attendance
from faker import Faker # type: ignore
def fakestudents(count):
    fake=Faker()
    studets=Student.objects.all()
    for s in studets:
        s.name=fake.name()
        s.save()   
        print("Done name is {s.name}") 
    
    
