import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from local_apps.profiles.models import Employee

class SupportGroup(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('Support Group')
        verbose_name_plural = ('Support Groups')
        permissions = (
            ("can_create_ticket", "Can create ticket"),
            ("can_delete_ticket", "Can delete ticket"),
            ("can_update_ticket", "Can update ticket"),
        )

class Ticket(models.Model):

    PRIORITY_CHOICES = (
        (1,('Baja')),
        (2,('Media')),
        (3,('Alta')),
        (4,('Extremadamente alta')),
    )

    STATUS_CHOICES = (
        (1,('Abierto')),
        (2,('Demorado')),
        (3,('Alta')),
        (4,('Transferido')),
        (5,('Cerrado')),
    )

    DATE_NOW = datetime.datetime.now()

    author = models.ForeignKey(Employee,on_delete=models.CASCADE,)
    assigned_to = models.ForeignKey(SupportGroup,on_delete=models.CASCADE)
    subject = models.CharField(max_length=144)
    message = models.TextField(max_length=700)
    ticket_number = models.IntegerField(blank=True,default=1)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1)
    print_screen = models.ImageField(upload_to='tickets_prtscr', null=True, blank=True)
    document = models.ImageField(upload_to='tickets_documents', null=True, blank=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = ('Ticket')
        verbose_name_plural = ('Tickets')
        permissions = (
            ("can_create_ticket", "Can create ticket"),
            ("can_delete_ticket", "Can delete ticket"),
            ("can_update_ticket", "Can update ticket"),
            ("can_change_ticket_status", "Can change ticket status"),
            ("can_asign_ticket", "Can asign ticket"),
            ("can_close_ticket", "Can close ticket"),
            ("can_reopen_ticket", "Can reopen ticket"),
            ("can_transfer_ticket", "Can transfer ticket"),
        )

# class Ticket_Reply(models.Model):
#
#     def __srt__(self):
#         pass
#
#     class Meta:
#         pass
#
#     pass
