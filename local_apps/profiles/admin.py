from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(ProfileType)
class ProfileAdmin(admin.ModelAdmin):
    fields = ('name', )
    list_display = ('name',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ('intra_user','first_name','last_name','bio','genre','profiletype','avatar')
    list_display = ('intra_user','first_name','last_name','bio','genre','profiletype','avatar')
