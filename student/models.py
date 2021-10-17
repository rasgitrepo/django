from django.db import models
from people .models import People

# Create your models here.
class StudentStatus(models.Model):
    student_status = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()

class Student(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE)
    homeroom = models.CharField(max_length=100, blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    ps_person_id = models.CharField(max_length=80, null=True, blank=True)
    ps_student_number = models.CharField(max_length=80, null=True, blank=True)
    student_status = models.ForeignKey(StudentStatus, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Course(models.Model):
    course = models.CharField(max_length=100, null=True, blank=True)
    grade = models.CharField(max_length=20, null=True, blank=True)
    school = models.CharField(max_length=20, null=True, blank=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class LinkStudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    from_date = models.DateTimeField(blank=True, null=True)
    to_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


