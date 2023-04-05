import random
from mainapp.models import Department

DEPARTMENT_NAMES = [
    "Physics",
    "Chemistry",
    "Biology",
    "Computer Science",
    "Mathematics",
    "Business Administration",
    "Economics",
    "Political Science",
    "International Relations",
    "Sociology",
    "Psychology",
    "English Literature",
    "History",
    "Philosophy",
    "Anthropology",
    "Environmental Science",
    "Architecture",
    "Engineering",
    "Journalism",
    "Education",
    "Law",
    "Music",
    "Art",
    "Foreign Languages",
    "Public Health",
]
for i in range(5):
    department_id = random.randint(1, 256)
    department_name = random.choice(DEPARTMENT_NAMES)
    d = Department(id=department_id, name=department_name)
    d.save()
