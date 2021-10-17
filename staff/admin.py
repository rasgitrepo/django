from django.contrib import admin
from .models import Staff, Department, StaffRole, linkStaffDepartment

class StaffAdmin(admin.ModelAdmin):
    list_display = ('people', 'pk', 'date_start','job_title')
    search_fields = ['people__firstname', 'people__lastname', 'people__nickname']
    ordering = ['people']

# FORMAT MODEL RECORDS FORMAT
class StaffRoleAdmin(admin.ModelAdmin):
    list_display = ('pk','staff_role' )
    ordering = ['staff_role']
    #list_filter = [ 'return_date', 'computer__type' ]
    #search_fields = ['computer_id', 'people__firstname', 'people__lastname']

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('pk','department', 'parent', 'description')
    list_filter = ['parent']
    ordering = ['department']
    #search_fields = ['tag_number','prev_tag', 'brand', 'model', 'serial_number' ]
 
class LinkStaffDepartmentAdmin(admin.ModelAdmin):
    list_display = ('pk','staff','department')
    #search_fields = ['firstname', 'lastname', 'nickname']

# Register your models here.
admin.site.register(Staff, StaffAdmin)
admin.site.register(StaffRole, StaffRoleAdmin)
admin.site.register(Department, DepartmentAdmin) 
admin.site.register(linkStaffDepartment, LinkStaffDepartmentAdmin)
