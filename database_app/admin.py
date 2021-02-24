from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Object)
admin.site.register(Company)
admin.site.register(People)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date']
    list_filter = ['start_date']


admin.site.register(Material)
admin.site.register(HiddenWorksSurveyCertificate)
admin.site.register(Template)
admin.site.register(ExecutiveScheme)
admin.site.register(Trials)
admin.site.register(Documents)
