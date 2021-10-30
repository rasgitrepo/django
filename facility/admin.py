from django.contrib import admin
from .models import Type, Facilities

class TypeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'type', 'description']
    list_display_links = ['pk', 'type', 'description']

class FacilityAdmin(admin.ModelAdmin):
    list_display = ['pk','title','type','location']
    list_display_links = ['pk','title','type','location']


# Register your models here.

admin.site.register(Type, TypeAdmin)
admin.site.register(Facilities, FacilityAdmin)