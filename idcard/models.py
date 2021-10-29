from django.db import models
from people .models import People
from staff .models import Staff
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File

# Create your models here.
class IDType(models.Model):
    id_type = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True) 
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.id_type

    class Meta:
        ordering=['id_type']   

class IDStatus(models.Model):
    id_status = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.id_status

    class Meta:
        ordering = ['id_status']

class IDCard(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE, related_name='card_holder')
    id_type = models.ForeignKey(IDType, on_delete=models.SET_NULL, null=True)
    request_date = models.DateField(null=True, blank=True)
    card_number = models.CharField(max_length=100, blank=True, null=True)
    id_status = models.ForeignKey(IDStatus, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True)
    issued_by = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, related_name='issued_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    barcode = models.ImageField(upload_to='images/', blank=True, null=True)
    
    def __str__(self):
        return str(self.people)

    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('ean13')   
        ean = EAN(f'{self.card_number}', writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save('barcode.png', File(buffer), save=False)
        return super().save(*args, **kwargs)

 
