from django.contrib import admin
from .models import *

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    fields = ('name','description','has_date_from','has_date_to','brand','status',)
    list_display = ('name','description','has_date_from','has_date_to','brand','status',)

@admin.register(Brand_Report)
class Brand_ReportAdmin(admin.ModelAdmin):
    fields = ('brand_associated',)
    list_display = ('brand_associated',)
