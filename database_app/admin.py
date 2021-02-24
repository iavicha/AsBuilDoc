from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from .views import some_view

# Register your models here.

from .models import *

admin.site.register(Object)
admin.site.register(Company)
admin.site.register(People)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['name', '_next', 'start_date', 'end_date']
    list_filter = ['start_date']


admin.site.register(Material)


def make_published(modeladmin, request, queryset):
    queryset.update(status='p')


make_published.short_description = "Пометить документы как распечатаные"


def make_signature(modeladmin, request, queryset):
    queryset.update(status='w')


make_signature.short_description = "Пометить документы как Подписанные"


def export_selected_objects(modeladmin, request, queryset):
    queryset.update(status='p')
    return some_view(request, queryset)


export_selected_objects.short_description = 'Распечатать документы'


class AdminHiddenWorksSurveyCertificate(admin.ModelAdmin):
    list_display = ['number', 'job', 'date_of_signature', 'status']
    list_filter = ['status']
    actions = [make_published, make_signature, export_selected_objects]


admin.site.register(HiddenWorksSurveyCertificate, AdminHiddenWorksSurveyCertificate)

admin.site.register(Template)
admin.site.register(ExecutiveScheme)
admin.site.register(Trials)
admin.site.register(Documents)
