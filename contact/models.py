from django.db import models
from people .models import People

# Create your models here.
class ContactType(models.Model):
    contact_type=models.CharField(max_length=50,null=True, blank=True)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.contact_type
    class Meta:
        ordering=['contact_type']    

class Contact(models.Model):
    people=models.ForeignKey(People, on_delete=models.CASCADE)
    contact_type=models.ForeignKey(ContactType, on_delete=models.CASCADE)
    contact=models.CharField(max_length=150, blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    