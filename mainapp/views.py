from django.shortcuts import render
from django.http import HttpRequest
from .models import Department, Faculty, Student, Course, Enrollment
import mainapp.myhash as myhash
from django.views.decorators.csrf import csrf_exempt
import random
from datetime import datetime


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
    context = {"action": "enrollments"}
    if request.method == "POST":
        username = request.POST["name"]
        password = request.POST["password"]
        print(username, password)
        student = Student.objects.get(pk=username)
        if myhash.check_hash(password, student.password):
            context = {"enrollments":
                       Enrollment.objects.filter(student_id=username)}
            return render(request, "enrollments.html", context)
    return render(request, "login.html", context)


@csrf_exempt
def detail_course(request: HttpRequest):
    course_id = int(request.path.split("/")[1][1:])
    course = Course.objects.get(id=course_id)
    context = {"course": course}
    if request.method == "POST":
        username = request.POST["name"]
        password = request.POST["password"]
        print(username, password)
        student = Student.objects.get(pk=username)
        if myhash.check_hash(password, student.password):
            enrollment = Enrollment(
                id=random.randint(1, 256),
                student_id=student,
                course_id=course,
                enrollment_date=datetime.now(),
                grade=0,
            )
            enrollment.save()
            return render(request, "success.html")
    return render(request, "course_detail.html", context)


@csrf_exempt
def student_login(request: HttpRequest):
    context = {"action": "login"}
    if request.method == "POST":
        username = request.POST["name"]
        password = request.POST["password"]
        print(username, password)
        student = Student.objects.get(pk=username)
        if myhash.check_hash(password, student.password):
            enr = Enrollment.objects.filter(
                student_id=student)
            gs, cs, pcs = [], [], []
            for ei in enr:
                g = ei.grade
                if g == 0:
                    pcs.append(ei.course_id)
                    continue
                gs.append(g)
                cs.append(ei.course_id.creds)
            cgpa = sum([gi * ci for gi, ci in zip(gs, cs)]) / sum(cs)
            context = {"student": student, "cgpa": cgpa, "courses": pcs}
            return render(request, "student.html", context)
    return render(request, "login.html", context)
