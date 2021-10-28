from django.contrib import admin
from student .models import Student, Grade, Course, LinkStudentCourse, StudentStatus, DropoffPickup

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'people','homeroom', 'date_start', 'date_end')
    list_display_links = ('pk', 'people','homeroom', 'date_start', 'date_end')
    ordering = ['pk']
    search_fields = ['people__firstname', 'people__lastname' ]

class GradeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'grade')
    list_display_links = ('pk', 'grade')
    ordering = ['grade']

class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'course','grade', 'teacher')
    list_display_links = ('pk', 'course','grade', 'teacher')
    ordering = ['pk']

class LinkStudentCourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'student','course', 'from_date', 'to_date')
    list_display_links = ('pk', 'student','course', 'from_date', 'to_date')
    list_filter = [ 'course' ]
    ordering = ['pk']

class StudentStatusAdmin(admin.ModelAdmin):
    list_display = ('pk', 'student_status')
    ordering = ['pk']

class DropoffPickupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'student', 'family_member', 'transaction_date')
    

# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(LinkStudentCourse, LinkStudentCourseAdmin)
admin.site.register(StudentStatus, StudentStatusAdmin)
admin.site.register(DropoffPickup, DropoffPickupAdmin)
