from django.conf.urls import url
from django.contrib import admin

from local_apps.reports import views as reports_views

urlpatterns = [
    url(r'^$', reports_views.report, name="Report"),
    url(r'^topshop$', reports_views.topshop_reports, name="Topshop"),
    url(r'^topshop/bwt$', reports_views.report_bwt, name="TopshopBWT"),
    url(r'^topshop/json/bwt$', reports_views.json_report_bwt, name="TopshopJsonBWT"),
]
