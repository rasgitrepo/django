from django.db import models

# Create your models here.
class ECAType(models.Model):
    eca_type=models.CharField(max_length=150, null=True, blank=True)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.eca_type
    class Meta:
        ordering=['eca_type']

class DayBF(models.Model):
    dayBF=models.IntegerField()
    name=models.CharField(max_length=50, blank=True, null=True)

class ECA(models.Model):
    eca=models.CharField(max_length=150, null=True, blank=True)
    eca_type=models.ForeignKey(ECAType, on_delete=models.CASCADE)
    dayBF=models.ForeignKey(DayBF, on_delete=models.CASCADE)
    date_from=models.DateField(blank=True, null=True)
    date_to=models.DateField(blank=True, null=True)
    time_from=models.TimeField(blank=True, null=True)
    time_to=models.TimeField(blank=True, null=True)
