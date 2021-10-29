from django.contrib import admin
from .models import Computer, Borrow


# CHANGE HEADER TITLE IN ADMIN SECTION
admin.site.site_header = 'RAS Management Information System'

# FORMAT MODEL RECORDS FORMAT
class ComputerAdmin(admin.ModelAdmin):
    list_display = ('pk','brand','model', 'prev_tag', 'tag_number')
    list_display_links = ('pk','brand','model', 'prev_tag', 'tag_number')
    list_filter = ['type', 'brand']
    search_fields = ['tag_number','prev_tag', 'brand', 'model', 'serial_number' ]
 
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('computer','staff','note','borrow_date','return_date' )
    list_filter = [ 'return_date', 'computer__type' ]
    search_fields = ['computer_id', 'people__firstname', 'people__lastname']




# Register your models here.
admin.site.register(Computer, ComputerAdmin)
admin.site.register(Borrow, BorrowAdmin) 

