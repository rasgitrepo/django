from django.db import models
from people .models import People
from staff .models import Staff

# Create your models here.
class StudentStatus(models.Model):
    student_status = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Student Status"

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

    def __str__(self):
        return self.people.firstname + ' ' + self.people.lastname
    

class Grade(models.Model):
    grade = models.CharField(max_length=50, blank=True, null=True)
    grade_id = models.IntegerField()

    def __str__(self):
        return self.grade
    

class Course(models.Model):
    course = models.CharField(max_length=100, null=True, blank=True)
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True) 
    teacher = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True) 
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course
    
class LinkStudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    from_date = models.DateTimeField(blank=True, null=True)
    to_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['student']    
        verbose_name_plural = "Add/Remove Student's course"


LOGTYPE = (
    ('Dropoff', 'Dropoff'),
    ('Pickup', 'Pickup')
)
class DropoffPickup(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    logtype = models.CharField(max_length=80, blank=True, null=True, choices=LOGTYPE)
    transaction_date = models.DateTimeField(auto_now_add=True)
    family_member = models.ForeignKey(People, on_delete=models.CASCADE)

