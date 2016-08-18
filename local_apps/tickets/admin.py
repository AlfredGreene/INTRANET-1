from django.contrib import admin

from .models import *

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    fields = ('author','subject','message','ticket_number','status','priority','created','print_screen',)
    list_display = ('author','subject','message','ticket_number','status','priority','created','print_screen',)
