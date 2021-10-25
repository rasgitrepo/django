from django.contrib import admin
from .models import Job, JobType, JobStatus, JobAction, jobActionLog

class JobAdmin(admin.ModelAdmin):
    list_display = ('pk','job_type','job_title', 'due_date') 
    list_display_links = ('pk','job_type','job_title', 'due_date')
    ordering = ['job_title']

class JobTypeAdmin(admin.ModelAdmin):
    list_display = ('pk','job_type')
    ordering = ['job_type']

class JobStatusAdmin(admin.ModelAdmin):
    list_display = ('pk', 'job_status', 'description')
    list_display_links = ('pk', 'job_status', 'description')
    ordering = ['pk']

class JobActionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'job_action','description')
    list_display_links =  ('pk', 'job_action','description')
    ordering = ['job_action']

class jobActionLogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'job', 'job_action', 'description')
    list_display_links = ('pk', 'job', 'job_action', 'description')
    
# Register your models here.
admin.site.register(Job, JobAdmin)
admin.site.register(JobType, JobTypeAdmin)
admin.site.register(JobStatus, JobStatusAdmin)
admin.site.register(JobAction, JobActionAdmin)
admin.site.register(jobActionLog, jobActionLogAdmin)


