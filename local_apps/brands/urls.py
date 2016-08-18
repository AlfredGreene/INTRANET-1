from django.conf.urls import url
from django.contrib import admin

from local_apps.brands import views as brands_views

urlpatterns = [
    url(r'^$', brands_views.home, name="Home"),
]
