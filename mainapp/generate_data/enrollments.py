import random
from mainapp.models import Department, Course, Student, Enrollment
from faker import Faker
import itertools

faker = Faker()
courses = list(Course.objects.all())
studs = list(Student.objects.all())
data = list(itertools.product(studs, courses))
ids = range(1, 256)
for i in range(20 * 200):
    id = random.sample(ids, 1)[0]
    s_d = random.sample(data, 1)[0]
    stud, course, date, grade = (
        s_d[0],
        s_d[1],
        faker.date(),
        random.randint(5, 11),
    )
    s = Enrollment(
        id=id,
        student_id=stud,
        course_id=course,
        enrollment_date=date,
        grade=grade,
    )
    s.save()
