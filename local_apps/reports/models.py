import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from local_apps.brands.models import Brand


class Brand_Report(models.Model):

    name = models.CharField(max_length=40)
    brand_associated = models.ForeignKey(Brand)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('Brand Report')
        verbose_name_plural = ('Brand Reports')
        permissions = (
            ("can_create_brand_report", "Can create brand report"),
            ("can_delete_brand_report", "Can delete brand report"),
            ("can_update_brand_report", "Can update brand report"),
        )



class Report(models.Model):

    STATUS_CHOICES = (
        (1,('Activo')),
        (2,('Inactivo')),
    )

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True)
    has_date_from = models.BooleanField(default=False)
    has_date_to = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand_Report)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('Report')
        verbose_name_plural = ('Reports')
        permissions = (
            ("can_create_report", "Can create reports"),
            ("can_delete_report", "Can delete reports"),
            ("can_update_report", "Can update reports"),
            ("can_change_report_status", "Can change report status"),
            ("can_asign_report", "Can asign reports"),
            ("can_close_report", "Can close reports"),
            ("can_reopen_report", "Can reopen reports"),
            ("can_transfer_report", "Can transfer reports"),
            ("can_see_administrative_report", "Can see administrative reports"),
            ("can_see_human_resources_report", "Can see human resources reports"),
            ("can_see_IT_report", "Can see IT reports"),
            ("can_see_commercial_report", "Can see commercial reports"),
        )
