from django.contrib import admin
from .models import People

admin.site.site_header = 'People Data Administration'

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'firstname','lastname')
    list_display_links = ('pk', 'firstname','lastname' )
    search_fields = ['firstname', 'lastname' ]

admin.site.register(People, PeopleAdmin)