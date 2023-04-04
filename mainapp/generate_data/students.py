import random
from faker import Faker
from mainapp.models import Department, Faculty, Student

fake = Faker()
STUDENTS = []
for i in range(20):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    dob = fake.date_of_birth()
    person = [first_name, last_name, email, dob]
    STUDENTS.append(person)

depts = list(Department.objects.all())
faculty = list(Faculty.objects.all())
for i in range(20):
    id = random.randint(1, 256)
    first_name, last_name, email, dob = STUDENTS[i]
    ph = random.randint(1000000000, 9999999999)
    s = Student(id=id, first_name=first_name, last_name=last_name,
                email=email, phone_number=ph, date_of_birth=dob, faculty_advisor_id=random.choice(faculty), department_id=random.choice(depts))
    s.save()
