from django.shortcuts import render
from django.http import HttpResponse

from erp.settings import BASE_DIR


def home(request):
    return render(request, str(BASE_DIR) + "/HTML/base.html")


def courses(request):
    return render(request, str(BASE_DIR) + "/HTML/courses.html")
