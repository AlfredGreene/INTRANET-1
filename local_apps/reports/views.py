# Django Imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.generic import *
import json
import datetime

from local_apps.reports import bwt

@login_required
def report(request):

    return render(request, 'frontend/report.html', {
        'title': 'Reportes',
    })


def topshop_reports(request):

    return render(request, 'reports/topshop/reports-topshop.html', {
        'title': 'Reportes',
    })


def report_bwt(request):

    return render(request, 'reports/topshop/bwt.html', {
        'title': 'BWT Reporte',
    })

    # report = json.loads(bwt.bwt_report('2016-07-03', '2016-07-09'))
    # data = json.dumps(report, sort_keys = True, indent = 4)
    # context = {
    #     'data':data,
    #     'title': 'reporte bwt',
    #     }
    # # return HttpResponse(report, content_type='application/json')
    # return render(request, , context)

@login_required
def json_report_bwt(request):

    report = json.loads(bwt.bwt_report('2016-07-03', '2016-07-09'))
    data = json.dumps(report, sort_keys = True, indent = 4)
    # context =
    # return HttpResponse(report, content_type='application/json')
    return HttpResponse({
        data
        }, content_type='application/json')
