from django.shortcuts import render
from django.http import HttpResponse

from erp.settings import BASE_DIR


def home(request):
    return render(request, "base.html")


def courses(request):
    return render(request, "courses.html")
