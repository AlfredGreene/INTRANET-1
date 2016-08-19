from django.contrib import admin

from .models import *

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    fields = ('name','dir1','dir2','country',)
    list_display = ('name','dir1','dir2','country',)

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    fields = ('name','organization','location','brand',)
    list_display = ('name','organization','location','brand',)

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    fields = ('name', 'legal_name', 'ruc')
    list_display = ('name', 'legal_name', 'ruc')
