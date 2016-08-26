# Django Imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import *
import datetime

from .models import *

@login_required
def tickets_list(request):

    ticket = Ticket.objects.all()
    return render(request, 'frontend/ticket.html', {
        'title': 'tickets',
        'tickets':ticket,
    })


@login_required
def ticket_add(request):

    return render(request, 'frontend/ticket.html', {
        'title': 'Crear ticket',
    })

@login_required
def ticket_detail(request, ticket_id):

    queryset = Ticket.objects.all()
    ticket = get_object_or_404(queryset, pk=ticket_id)

    return render(request, 'tickets/details.html', {
        'title': 'Crear ticket',
        'ticket': ticket,
    })

@login_required
def ticket_edit(request, ticket_id):

    return render(request, 'frontend/ticket.html', {
        'title': 'Crear ticket',
    })
