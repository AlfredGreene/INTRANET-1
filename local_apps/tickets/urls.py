from django.conf.urls import url
from django.contrib import admin

from local_apps.tickets import views as tickets_views
from local_apps.tickets import models as Ticket

urlpatterns = [
    url(r'^$', tickets_views.tickets_list, name="Ticket"),
    url(r'^add/$', tickets_views.ticket_add, name="CreateTicket"),
    url(r'^(?P<ticket_id>[0-9]+)/$', tickets_views.ticket_detail, name="TicketDetail"),
    url(r'^(?P<ticket_id>[0-9]+)/edit$', tickets_views.ticket_edit, name="EditTicket"),
]
