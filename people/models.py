from django.db import models
from django.utils.timezone import now

# Create your models here.
GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

TITLE = (
    ('Mr.', 'Mr.'),
    ('Miss', 'Miss.'),
    ('Mrs.', 'Mrs.'),
    ('Ms.', 'Ms.'),
    ('Khun.', 'Khun.'),
    ('Dr.', 'Dr.'),
)
class People(models.Model):
    firstname = models.CharField(max_length=150, null=True,  blank=True)
    lastname = models.CharField(max_length=150, null=True,  blank=True)
    nickname = models.CharField(max_length=100, null=True,  blank=True)
    gender = models.CharField(max_length=15, choices=GENDER, null=True,  blank=True)
    title = models.CharField(max_length=25,choices=TITLE, null=True,  blank=True)
    dob = models.DateField(null=True, blank=True) 
    updated_at = models.DateTimeField(default=now)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.firstname +  ' ' + str(self.lastname) + ' (' +str(self.id) + ')'
    