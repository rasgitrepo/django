from django.db import models
from staff .models import Staff

TYPE = (
    ('Create New Staff','Create New Staff'),
    ('New Staff Email','New Staff Email'),
    ('New Staff PowerSchool','New Staff PowerSchool'),
    ('Reset Email Password','Reset Email Password'),
    ('Reset PowerSchool Password','Reset PowerSchool Password'),
    
)

# Create your models here.
class JobType(models.Model):
    job_type = models.CharField(max_length=100, blank=True, null=True)
    parent_type = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()

class JobStatus(models.Model):
    job_status = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(null=True, blank=True)

class Job(models.Model):
    job_type = models.ForeignKey(JobType, on_delete=models.SET_NULL, blank=True, null=True)
    job_title = models.CharField(max_length=150, null=True, blank=True)
    requester = models.ForeignKey(Staff, on_delete=models.SET_NULL, blank=True, null=True)
    due_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    job_status = models.ForeignKey(JobStatus, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class JobAction(models.Model):
    job_action = models.CharField(max_length=150, null=True)
    description = models.CharField(max_length=255, null=True)

class jobActionLog(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    job_action = models.ForeignKey(JobAction, on_delete=models.CASCADE)
    description = models.TextField()
    action_by = models.ForeignKey(Staff, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
