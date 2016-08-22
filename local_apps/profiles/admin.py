from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(ProfileType)
class ProfileAdmin(admin.ModelAdmin):
    fields = ('name', )
    list_display = ('name',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ('first_name','last_name','bio','genre','profiletype','avatar','birthday')
    list_display = ('first_name','last_name','bio','genre','profiletype','avatar','birthday')
