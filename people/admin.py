from django.contrib import admin
from .models import People, Family, LinkFamilyMember

admin.site.site_header = 'People Data Administration'

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'firstname','lastname')
    list_display_links = ('pk', 'firstname','lastname' )
    search_fields = ['firstname', 'lastname' ]

class FamilyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'family', 'father', 'mother')
    list_display_links = ('pk', 'family')
    search_fields = ['family']

class LinkFamilyMemberAdmin(admin.ModelAdmin):
    list_display = ('pk', 'family', 'people', 'role')
    search_fields = ['family__family' ]
    #list_display_links = ('pk', 'family__family', 'people', 'role')

admin.site.register(People, PeopleAdmin)
admin.site.register(Family,FamilyAdmin)
admin.site.register(LinkFamilyMember,LinkFamilyMemberAdmin)