from django.contrib import admin

from .models import *

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    fields = ('name', 'logo')
    list_display = ('name',)
