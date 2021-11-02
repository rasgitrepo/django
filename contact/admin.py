from django.contrib import admin
from .models import Contact, ContactType
from people .models import People

class ContactAdmin(admin.ModelAdmin):
    list_display=('pk','people','contact_type','contact')
    list_display_links=('pk','people','contact_type','contact')

    class Meta:
        ordering=['people','contact_type']    

class ContactTypeAdmin(admin.ModelAdmin):
    list_display=('pk','contact_type')
    list_display_links=('pk','contact_type')
    class Meta:
        ordering=['contact_type']    
    

# Register your models here.
admin.site.register(ContactType, ContactTypeAdmin)
admin.site.register(Contact, ContactAdmin)