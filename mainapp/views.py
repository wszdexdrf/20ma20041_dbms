from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Department, Faculty
from erp.settings import BASE_DIR


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
