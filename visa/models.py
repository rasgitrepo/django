from django.db import models
from staff .models import Staff

# Create your models here.
class Visa(models.Model):
    staff=models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    visa_number=models.CharField(max_length=100, null=True, blank=True)
    expiry_date=models.DateField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff
        ordering=['expiry_date','staff']
    