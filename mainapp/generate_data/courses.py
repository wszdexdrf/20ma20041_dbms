import random
from mainapp.models import Department, Course
import string


def random_string(length):
    letters = string.ascii_lowercase + string.digits
    return "".join(random.choice(letters) for i in range(length))


ids = range(1, 256)
depts = list(Department.objects.all())
for i in range(20):
    id = random.sample(ids, 1)[0]
    name, desc, creds = (
        random_string(7),
        random_string(50),
        random.randint(1, 6),
    )
    random.randint(1, 6)
    s = Course(
        id=id,
        course_name=name,
        description=desc,
        department_id=random.choice(depts),
        creds=creds,
    )
    s.save()
