from django.shortcuts import render
from django.http import HttpRequest
from .models import Department, Faculty, Student, Course, Enrollment
import mainapp.myhash as myhash
from django.views.decorators.csrf import csrf_exempt


def home(request):
    departments = Department.objects.all()
    context = {"departments": departments}
    return render(request, "base.html", context)


def courses(request):
    courses = Course.objects.all()
    context = {"courses": courses}
    return render(request, "courses.html", context)


def department(request: HttpRequest):
    dept_id = int(request.path.split("/")[1])
    dept = Department.objects.get(id=dept_id)
    faculty = Faculty.objects.filter(department_id=dept_id)
    context = {"department": dept, "faculty": faculty}
    return render(request, "department.html", context)


@csrf_exempt
def login_view(request: HttpRequest):
    if request.method == "POST":
        username = request.POST["name"]
        password = request.POST["password"]
        print(username, password)
        student = Student.objects.get(pk=username)
        if myhash.check_hash(password, student.password):
            context = {"enrollments":
                       Enrollment.objects.filter(student_id=username)}
            return render(request, "enrollments.html", context)
    return render(request, "enr_login.html")
