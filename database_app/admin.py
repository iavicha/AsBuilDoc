from django.contrib import admin

from .models import *
from .views import some_view

# Register your models here.

admin.site.register(Object)
admin.site.register(Company)
admin.site.register(People)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ["name", "_next", "start_date", "end_date"]
    list_filter = ["start_date"]


admin.site.register(Material)


def make_published(modeladmin, request, queryset):
    queryset.update(status="p")


make_published.short_description = "Пометить документы как распечатаные"


def make_signature(modeladmin, request, queryset):
    queryset.update(status="w")


make_signature.short_description = "Пометить документы как Подписанные"


def make_draft(modeladmin, request, queryset):
    queryset.update(status="d")


make_draft.short_description = "Пометить документы как черновик"


def export_selected_objects(modeladmin, request, queryset):
    queryset.update(status="p")

    for i in queryset.values():
        print(i["id"])

    return some_view(request, queryset)


export_selected_objects.short_description = "Распечатать документы"


class AdminHiddenWorksSurveyCertificate(admin.ModelAdmin):
    list_display = ["number", "job", "date_of_signature", "status"]
    list_filter = ["status"]
    actions = [make_published, make_signature, make_draft, export_selected_objects]


admin.site.register(HiddenWorksSurveyCertificate, AdminHiddenWorksSurveyCertificate)

admin.site.register(Template)

admin.site.register(ExecutiveScheme)
admin.site.register(Trials)
admin.site.register(Documents)
