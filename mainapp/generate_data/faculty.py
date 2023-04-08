import random
from mainapp.models import Faculty, Department
from faker import Faker

fake = Faker()
FACULTY_NAMES = []
for i in range(100):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    dob = fake.date_of_birth()
    person = [first_name, last_name, email]
    FACULTY_NAMES.append(person)
depts = list(Department.objects.all())
ids = range(1, 256)
for i in range(100):
    id = random.sample(ids, 1)[0]
    first_name, last_name, email = FACULTY_NAMES[i]
    ph = random.randint(1000000000, 9999999999)
    f = Faculty(
        id=id,
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone_number=ph,
        department_id=random.choice(depts),
    )
    f.save()
