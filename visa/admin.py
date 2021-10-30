from django.contrib import admin
from .models import Visa

class VisaAdmin(admin.ModelAdmin):
    list_display=('pk','staff','visa_number','expiry_date')
    list_display_links=('pk','staff','visa_number','expiry_date')

# Register your models here.
admin.site.register(Visa,VisaAdmin)