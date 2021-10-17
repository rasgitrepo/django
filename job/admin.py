from django.contrib import admin
from .models import JobType, JobStatus, JobAction, jobActionLog
 
class JobTypeAdmin(admin.ModelAdmin):
    list_display = ('pk','job_type')

class JobStatusAdmin(admin.ModelAdmin):
    list_display = ('pk', 'job_status')

class JobActionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'job_action')

class jobActionLogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'job_action')

# Register your models here.
admin.site.register(JobType, JobTypeAdmin)
admin.site.register(JobStatus, JobStatusAdmin)
admin.site.register(JobAction, JobActionAdmin)
admin.site.register(jobActionLog, jobActionLogAdmin)


