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