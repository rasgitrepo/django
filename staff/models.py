from django.db import models
from people .models import People
from django.utils.timezone import now

# Create your models here.
class Staff(models.Model):
    people = models.ForeignKey(People, on_delete=models.SET_NULL, null=True) 
    date_start = models.DateField(null=True, blank=True) 
    date_end = models.DateField(null=True, blank=True)
    job_title = models.CharField(max_length=150, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(default=now)
    created_at = models.DateTimeField(default=now)
    

    def __str__(self):

            return self.people.firstname+' '+str(self.people.lastname)

class StaffRole(models.Model):
    staff_role = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.staff_role
    

class Department(models.Model):
    department = models.CharField(max_length=150, null=True, blank=True)
    parent = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.department
        
class linkStaffDepartment(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    staff_role = models.ForeignKey(StaffRole, on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(default=now)
    created_at = models.DateTimeField(default=now)
    active = models.BooleanField(default=True)
