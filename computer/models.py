from django.db import models
from django.utils.timezone import now

# Create your models here.
#Computer model
class Computer(models.Model):
    type = models.CharField(max_length=100, null=True,  blank=True)
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
    status = models.CharField(max_length=150, null=True,  blank=True)
    note = models.TextField()
    active = models.BooleanField(default=True)
    createdAt = models.DateTimeField(default=now, null=True, blank=True)
    updatedAt = models.DateTimeField(default=now, null=True,  blank=True)

class Rental(models.Model):


    def __str__(self):
        return self.model

    def snippet(self):
        return self.model[:4]
