from django.contrib import admin
from .models import Supplier, PurchasingOrder

class SupplierAdmin(admin.ModelAdmin):
    list_display=('pk','name','address')
class PurchasingOrderAdmin(admin.ModelAdmin):
    list_display=('pk','requester', 'po_ref_no', 'department')

# Register your models here.
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(PurchasingOrder, PurchasingOrderAdmin)