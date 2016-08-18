from django.conf.urls import url
from django.contrib import admin

from local_apps.dashboard import views as dashboard_views

urlpatterns = [
    url(r'^$', dashboard_views.dashboard, name="Dashboard"),
]
