from django.db import models
from staff .models import Staff
from django.utils.timezone import now

# Create your models here.
TYPE = (
    ('Laptop', 'Laptop'),
    ('All-in-one', 'All-in-one'),
    ('Desktop', 'Desktop'),
    ('Tablet', 'Tablet'),
    ('Document Camera', 'Document Camera'),
    ('Projector', 'Projector'),
    ('Printer', 'Printer'),    
)

ISSUE_BY = (
    ('Diaw', 'Diaw'),
    ('Jonathan', 'Jonathan'),
    ('Jo', 'Jo'),
    ('Em', 'Em Kanapot')

)

class Computer(models.Model):
    type = models.CharField(max_length=100, null=True,  blank=True, choices=TYPE)
    brand = models.CharField(max_length=100, null=True,  blank=True)
    model = models.CharField(max_length=150, null=True,  blank=True)
    cpu = models.CharField(max_length=150, null=True,  blank=True)
    ram = models.CharField(max_length=150, null=True,  blank=True)
    harddisk = models.CharField(max_length=150, null=True,  blank=True)
    serial_number = models.CharField(max_length=150, null=True,  blank=True)
    tag_number = models.CharField(max_length=150, null=True,  blank=True)
    location = models.CharField(max_length=150, null=True,  blank=True)
    owner = models.CharField(max_length=150, null=True,  blank=True)
    admin_user = models.CharField(max_length=150, null=True,  blank=True)
    admin_pass = models.CharField(max_length=150, null=True,  blank=True)
    computer_name = models.CharField(max_length=150, null=True,  blank=True)
    prev_tag = models.CharField(max_length=150, null=True,  blank=True)
    asset_number = models.CharField(max_length=150, null=True,  blank=True)
    note = models.TextField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.brand + ' ' + self.model + ' (' + self.tag_number + ')'
    
    class Meta:
       ordering = ('brand','model')
      

class Borrow(models.Model):
    
    computer = models.ForeignKey(Computer, on_delete=models.SET_NULL, null=True)
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    borrow_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    accessories = models.CharField(max_length=150, blank=True, null=True)
    issued_by = models.CharField(max_length=100,choices=ISSUE_BY, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

class Location(models.Model):
    location = models.CharField(max_length=150, null=True, blank=True)
    floor = models.CharField(max_length=80, null=True, blank=True)
    building = models.CharField(max_length=100, null=True, blank=True)

class Maintenance(models.Model):
    computer = models.ForeignKey(Computer, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField()
    requester = models.ForeignKey(Staff, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

