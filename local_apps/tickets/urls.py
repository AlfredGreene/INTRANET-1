from django.conf.urls import url
from django.contrib import admin

from local_apps.tickets import views as tickets_views

urlpatterns = [
    url(r'^$', tickets_views.ticket, name="Ticket"),
]
