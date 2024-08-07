from faker import Faker 
from students.models import Books 
from data import books_data

fake=Faker() 

for name in books_data:
    Books.objects.create(
        name=name,
        author=fake.name(),
        publication_year=fake.year(),
        quantity=fake.random_int(min=1, max=100)  # Random quantity between 1 and 100
    ) 
