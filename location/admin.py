from django.contrib import admin
from .models import LocationType, Location, Building

class BuildingAdmin(admin.ModelAdmin):
    list_display=['pk','building', 'school']
    list_display_links=['pk','building', 'school']

class LocationTypeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'location_type', 'description']
    list_display_links = ['pk', 'location_type', 'description']
    ordering = ['location_type']

class LocationAdmin(admin.ModelAdmin):
    list_display = ['pk','location','floor', 'building', 'description']    
    list_display_links = ['pk','location','floor', 'building', 'description']    
    ordering = ['location']

# Register your models here.
admin.site.register(Building, BuildingAdmin)
admin.site.register(LocationType, LocationTypeAdmin)
admin.site.register(Location, LocationAdmin)