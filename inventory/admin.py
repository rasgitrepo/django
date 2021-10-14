from django.contrib import admin
from .models import Computer, Borrow
from people .models import People
from staff .models import Staff

# CHANGE HEADER TITLE IN ADMIN SECTION
#admin.site.site_header = 'RAS Inventory Dashboard'

# FORMAT MODEL RECORDS FORMAT
class ComputerAdmin(admin.ModelAdmin):
    list_display = ('pk','brand','model', 'prev_tag', 'tag_number')
    list_filter = ['type', 'brand']
    search_fields = ['tag_number','prev_tag', 'brand', 'model', 'serial_number' ]
 
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('computer','staff','note','borrow_date','return_date' )
    list_filter = [ 'return_date', 'computer__type' ]
    search_fields = ['computer_id', 'people__firstname', 'people__lastname']

class StaffAdmin(admin.ModelAdmin):
    list_display = ('pk', 'people', 'date_start','job_title')
    search_fields = ['firstname', 'lastname', 'nickname']

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('pk','firstname','lastname')
    search_fields = ['firstname', 'lastname' ]

# Register your models here.
admin.site.register(Computer, ComputerAdmin)
admin.site.register(Borrow, BorrowAdmin) 
admin.site.register(Staff, StaffAdmin)
admin.site.register(People, PeopleAdmin)