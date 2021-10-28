from django.contrib import admin
from .models import IDType, IDStatus, IDCard

class IDTypeAdmin(admin.ModelAdmin):
    list_display = ['pk','id_type','description']
    list_display_links = ['pk','id_type','description']
    ordering = ['id_type',]

class IDStatusAdmin(admin.ModelAdmin):
    list_display = ['pk','id_status','description']
    list_display_links = ['pk','id_status','description']
    ordering = ['id_status',]

class IDCardAdmin(admin.ModelAdmin):
    list_display = ['pk','people', 'id_type', 'id_status']
    list_display_links = ['pk','people', 'id_type', 'id_status']
    ordering = ['request_date',]
    list_filer = ['id_type', 'id_status']
    search_fields =['people__firstname','people__lastname', 'people_nickname']


# Register your models here.
admin.site.register(IDType, IDTypeAdmin)
admin.site.register(IDStatus, IDStatusAdmin)
admin.site.register(IDCard, IDCardAdmin)
