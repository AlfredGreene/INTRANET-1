import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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
        (4,('Transfrido')),
        (5,('Cerrado')),
    )

    DATE_NOW = datetime.datetime.now()

    # TICKET_NUMBER_ID = Ticket.objects.latest('id')
    # TICKET_NUMBER_IDENTIFER = TICKET_NUMBER_ID + 1

    author = models.ForeignKey(User)
    subject = models.CharField(max_length=144)
    message = models.TextField(max_length=700)
    ticket_number = models.IntegerField(blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1)
    created = models.DateTimeField(default=DATE_NOW)
    print_screen = models.ImageField(upload_to='ticket/prtscr/', null=True, blank=True)


    def __str__(self):
        return self.name

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
