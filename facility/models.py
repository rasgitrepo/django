from django.db import models
from location .models import Location
# Create your models here.
class Type(models.Model):
    type=models.CharField(max_length=150, blank=True, null=True)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.type
    class Meta:
        ordering = ['type']    
        verbose_name_plural = "Facility Types"

class Facilities(models.Model):
    title=models.CharField(max_length=150, null=True, blank=True)
    description=models.TextField(blank=True)
    type=models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    location=models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    tag_number=models.CharField(max_length=80, blank=True, null=True)
    created_at=models.DateField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']    
        verbose_name_plural = "Facilities"
