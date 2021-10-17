from django.contrib import admin
from student .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'people','homeroom', 'date_start', 'date_end')


# Register your models here.
admin.site.register(Student, StudentAdmin)
