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

ids = range(1, 256)
for i in range(5):
    id = random.sample(ids, 1)[0]
    department_name = random.sample(DEPARTMENT_NAMES, 1)[0]
    d = Department(id=id, name=department_name)
    d.save()
