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


@login_required
def topshop_reports(request):

    return render(request, 'reports/topshop/reports-topshop.html', {
        'title': 'Reportes',
    })


@login_required
def report_bwt(request):

    if request.method == 'GET':

        return render(request, 'reports/topshop/reports-topshop.html', {'title':'Error!'} )

    elif request.method == 'POST':

        date_from = request.POST['date_from']
        date_to = request.POST['date_to']
        report = json.loads(bwt.bwt_report(date_from, date_to))
        data = json.dumps(report, sort_keys = True, indent = 4)
        # report = json.loads(bwt.bwt_report('2016-07-03', '2016-07-09'))
        # data = json.dumps(report, sort_keys = True, indent = 4)
        context = {
            'title': 'BWT Reporte',
            'date_from':date_from,
            'date_to':date_to,
            'data':data,
        }
        # # return HttpResponse(report, content_type='application/json')
        # return render(request, , context)
        return render(request, 'reports/topshop/bwt.html', context )


@login_required
def json_report_bwt(request):

    if request.method == 'GET':
        return render(request, 'reports/topshop.html',{'title':'Error!'})

    if request.method == 'POST':

        date_from = request.POST['date_from']
        date_to = request.POST['date_to']

        # context =
        # return HttpResponse(report, content_type='application/json')
        return HttpResponse({data}, content_type='application/json')
