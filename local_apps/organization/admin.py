from django.contrib import admin

from .models import *

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    fields = ('name', 'legal_name', 'ruc')
    list_display = ('name', 'legal_name', 'ruc')
