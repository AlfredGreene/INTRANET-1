from django import forms
from django.contrib.auth.models import User

from .models import *

class CreateTickets(forms.Form):

    author = forms.CharField(label='author', widget=forms.HiddenInput,)
    assigned_to = forms.CharField(label='assigned_to')
    subject = forms.CharField(label='subject')
    message = forms.CharField(widget=forms.Textarea, label="message")
    ticket_number = forms.CharField(label='ticket_number')
    status = forms.CharField(label='status')
    priority = forms.CharField(label='subject')
    print_screen = forms.CharField(label='subject')
    document = forms.CharField(label='subject')
    pub_date = forms.CharField(label='subject', widget=forms.HiddenInput)
    modified = forms.CharField(label='subject', widget=froms.HiddenInput)

    def get_users():
        users = User.objects.all()
        return users
