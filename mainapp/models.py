from django.db import models


class Faculty(models.Model):
    faculty_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12)
    department_id = models.ForeignKey("Department", on_delete=models.CASCADE)


class Department(models.Model):
    department_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    dept_head_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)


class Course(models.Model):
    course_id = models.BigAutoField(primary_key=True)
    course_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    credits = models.IntegerField()
    departmend_id = models.OneToOneField(Department)
