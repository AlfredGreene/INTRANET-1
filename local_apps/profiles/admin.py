from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(ProfileType)
class ProfileAdmin(admin.ModelAdmin):
    fields = ('name', )
    list_display = ('name',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ('name','bio','genre','profile',)
    list_display = ('name','bio','genre','profile',)
