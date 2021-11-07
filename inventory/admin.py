from django.contrib import admin
from .models import Computer, Borrow
from staff .models import Staff
from people .models import People

# CHANGE HEADER TITLE IN ADMIN SECTION
admin.site.site_header = 'RAS Management Information System'

# FORMAT MODEL RECORDS FORMAT
class ComputerAdmin(admin.ModelAdmin):
    list_display = ('pk','brand','model', 'prev_tag', 'tag_number')
    list_display_links = ('pk','brand','model', 'prev_tag', 'tag_number')
    list_filter = ['type', 'brand']
    search_fields = ['tag_number','prev_tag', 'brand', 'model', 'serial_number','computer_name','pk' ]
 
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('computer','staff','note','borrow_date','return_date' )
    list_filter = [ 'return_date', 'computer__type' ]
     
    search_fields = ['staff']




# Register your models here.
admin.site.register(Computer, ComputerAdmin)
admin.site.register(Borrow, BorrowAdmin) 
 
