import random
from mainapp.models import Faculty, Department

FACULTY_NAMES = [
    ["Charlotte", "Ramirez", "charlotte.ramirez23@gmail.com"],
    ["Mason", "Patel", "mason.patel87@yahoo.com"],
    ["Kira", "Khan", "kira.khan34@hotmail.com"],
    ["Caleb", "Wang", "caleb.wang51@gmail.com"],
    ["Sophia", "Singh", "sophia.singh12@outlook.com"],
    ["Oliver", "Lee", "oliver.lee76@yahoo.com"],
    ["Isla", "Gupta", "isla.gupta29@gmail.com"],
    ["Ethan", "Kim", "ethan.kim18@hotmail.com"],
    ["Ava", "Sharma", "ava.sharma83@gmail.com"],
    ["Benjamin", "Park", "benjamin.park45@outlook.com"],
    ["Lily", "Chen", "lily.chen57@yahoo.com"],
    ["William", "Rodriguez", "william.rodriguez92@gmail.com"],
    ["Amelia", "Nguyen", "amelia.nguyen20@hotmail.com"],
    ["Jackson", "Patel", "jackson.patel39@gmail.com"],
    ["Harper", "Chang", "harper.chang65@yahoo.com"],
    ["Noah", "Patel", "noah.patel54@outlook.com"],
    ["Madison", "Kim", "madison.kim96@gmail.com"],
    ["Samuel", "Patel", "samuel.patel48@yahoo.com"],
    ["Elizabeth", "Lee", "elizabeth.lee26@gmail.com"],
    ["Elijah", "Gupta", "elijah.gupta73@hotmail.com"],
]
depts = list(Department.objects.all())
for i in range(20):
    id = random.randint(1, 256)
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
