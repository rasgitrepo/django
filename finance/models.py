from django.db import models
from staff .models import Staff, Department
import datetime
from decimal import Decimal

# Create your models here.
class Supplier(models.Model):
    name=models.CharField(max_length=150, null=True, blank=True)
    address=models.CharField(max_length=150, null=True, blank=True)
    telephone=models.CharField(max_length=100, null=True, blank=True)
    email=models.CharField(max_length=100, null=True, blank=True)
    contact_name=models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']    
    
class PurchasingOrder(models.Model):
    requester=models.ForeignKey(Staff, on_delete=models.CASCADE)
    request_date=models.DateField(default=datetime.date.today)
    po_ref_no=models.CharField(max_length=100,blank=True, null=True)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)
    supplier=models.ForeignKey(Supplier, on_delete=models.CASCADE)
    total=models.DecimalField(max_digits=20, decimal_places=4, default=0.0)
    vat7percent=models.DecimalField(max_digits=20, decimal_places=4, default=0.0)
    amount_approved=models.DecimalField(max_digits=20, decimal_places=4, default=0.0)
    wht3percent=models.DecimalField(max_digits=20, decimal_places=4, default=0.0)
    net_amount=models.DecimalField(max_digits=20, decimal_places=4, default=0.0)
    pre_approved_vendor=models.BooleanField(default=False)
    provide3quotes=models.BooleanField(default=True)
    within_MREL=models.DecimalField(max_digits=20, decimal_places=4, default=0.0)
    MREL_limit=models.DecimalField(max_digits=20, decimal_places=4, default=0.0)
    exceed_MREL=models.DecimalField(max_digits=20, decimal_places=4, default=0.0)
    remark=models.CharField(max_length=150, null=True, blank=True)


