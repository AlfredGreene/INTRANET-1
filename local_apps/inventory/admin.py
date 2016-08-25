from django.contrib import admin

from .models import *
# Register your models here.
@admin.register(SO)
class SOAdmin(admin.ModelAdmin):
    fields = ('name','brand')
    list_display = ('name','brand')

@admin.register(Red_Interface)
class Red_InterfaceAdmin(admin.ModelAdmin):
    fields = ('name','public_ip','private_ip','range_ip')
    list_display = ('name','public_ip','private_ip','range_ip')

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    fields = ('name','ws_type','usb_ports','red_interface','lan','wlan','ram','cpu','hdd','so','brand','model','version','user','user_pass','sn','employee','organization','status',)
    list_display = ('name','ws_type','usb_ports','red_interface','lan','wlan','ram','cpu','hdd','so','brand','model','version','user','user_pass','sn','employee','organization','status',)
