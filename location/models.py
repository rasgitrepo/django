from django.db import models

# Create your models here.
class LocationType(models.Model):
    location_type = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.location_type
    class Meta:
        ordering = ['location_type']    

class Building(models.Model):
    building = models.CharField(max_length=100, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.building
    class Meta:
        ordering = ['building']    
    

class Location(models.Model):
    location = models.CharField(max_length=100, blank=True, null=True)
    floor = models.CharField(max_length=50, blank=True, null=True)
    building = models.ForeignKey(Building, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.location
    class Meta:
        ordering = ['location']

    
    

    
