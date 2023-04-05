from django.shortcuts import render
from django.http import HttpRequest
from .models import Department, Faculty
from django.views.decorators.csrf import csrf_exempt


def home(request):
    departments = Department.objects.all()
    context = {"departments": departments}
    return render(request, "base.html", context)


def courses(request):
    return render(request, "courses.html")


def department(request: HttpRequest):
    dept_id = int(request.path.split('/')[1])
    dept = Department.objects.get(id=dept_id)
    faculty = Faculty.objects.filter(department_id=dept_id)
    context = {"department": dept, "faculty": faculty}
    return render(request, "department.html", context)


@csrf_exempt
def login(request: HttpRequest):
    if request.method == "POST":
        print(request.POST)
    return render(request, "login.html")
