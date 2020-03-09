from django.contrib import admin
from .models import Applications


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name','number','email','admin_no','langauges','team','bio']
    list_filter = ['number', 'langauges', 'admin_no']
    list_editable = ['langauges', 'number', 'team']



admin.site.register(Applications, ApplicationAdmin)

 
