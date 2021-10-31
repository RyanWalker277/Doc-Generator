from django.contrib import admin

from .models import Audit, Pdf, GenericConfig


class AuditAdmin(admin.ModelAdmin):
    fields = ['id', 'status', 'pdf']


class PdfAdmin(admin.ModelAdmin):
    fields = ['id', 'status', 'tries']


class GenericConfigAdmin(admin.ModelAdmin):
    fields = ['id', 'name', 'data']


admin.site.register(Pdf, PdfAdmin)
admin.site.register(Audit, AuditAdmin)
admin.site.register(GenericConfig, GenericConfigAdmin)

