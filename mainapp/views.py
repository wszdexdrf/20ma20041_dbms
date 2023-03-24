from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "HTML/base.html")


def courses(request):
    return render(request, "HTML/courses.html")
