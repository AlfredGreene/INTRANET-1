from django.contrib import admin

from .models import *

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    fields = ('author','assigned_to','subject','message','ticket_number','status','priority','print_screen','document','pub_date')
    list_display = ('author','assigned_to','subject','message','ticket_number','status','priority','print_screen','document','pub_date')

@admin.register(SupportGroup)
class SupportGroupAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
