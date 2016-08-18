# Django Imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.generic import *
import datetime


@login_required
def home(request):
    name = 'Josmer'
    template = 'frontend/index.html'
    context = {
        'title': 'inicio'
    }
    return render(request, template, context )
