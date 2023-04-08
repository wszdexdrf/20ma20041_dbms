import random
from faker import Faker
from mainapp.models import Department, Faculty, Student
import string
import mainapp.myhash as myhash


def random_string(length):
    letters = string.ascii_lowercase + string.digits
    return "".join(random.choice(letters) for i in range(length))


f = open("passwords.txt", "w")
fake = Faker()
STUDENTS = []
for i in range(200):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    dob = fake.date_of_birth()
    password = random_string(8)
    person = [first_name, last_name, email, dob, password]
    STUDENTS.append(person)


depts = list(Department.objects.all())
faculty = list(Faculty.objects.all())
ids = range(1, 256)
for i in range(200):
    id = random.sample(ids, 1)[0]
    first_name, last_name, email, dob, password = STUDENTS[i]
    ph = random.randint(1000000000, 9999999999)
    s = Student(
        id=id,
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone_number=ph,
        date_of_birth=dob,
        faculty_advisor_id=random.choice(faculty),
        department_id=random.choice(depts),
        password=myhash.get_hash(password),
    )
    s.save()
    f.write(str(id) + ", " + password + "\n")
f.close()
