from django.db import models

from local_apps.brands.models import Brand
from local_apps.profiles.models import Employee
from local_apps.organization.models import Organization

class Red_Interface(models.Model):

    name = models.CharField(max_length=50)
    public_ip = models.CharField(max_length=15,blank=True)
    private_ip = models.CharField(max_length=15,blank=True)
    range_ip = models.CharField(max_length=3, default=24,blank=True)

    def __srt__(self):
        return self.name

    class Meta:

        verbose_name = ('Red Interface')
        verbose_name_plural = ('Red Interfaces')
        permissions = (
            ("can_create_red_interface", "Can create red interface"),
            ("can_delete_red_interface", "Can delete red interface"),
            ("can_update_red_interface", "Can update red interface"),
        )

class SO(models.Model):

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __srt__(self):
        return self.name

    class Meta:

        verbose_name = ('SO')
        verbose_name_plural = ('SO')
        permissions = (
            ("can_create_SO", "Can create SO"),
            ("can_delete_SO", "Can delete SO"),
            ("can_update_SO", "Can update SO"),
        )

class Equipment(models.Model):

    WORKSTATION_CHOICE_FIELDS = (
        (1, ('PC')),
        (2, ('Laptop')),
        (3, ('Teléfono')),
        (4, ('Router')),
        (5, ('Server')),
        (6, ('Lector biométrico')),
        (7, ('Batería de respaldo "Apc-upc"')),
        (8, ('Impresora Fiscal')),
        (9, ('Impresora multifuncional')),
        (10, ('Punto de venta')),
        (11, ('Lector códigos de barra')),
        (12, ('DVR')),
        (13, ('Impresora zebra')),
    )

    STATUS_CHOICE_FIELDS = (
        (1,('Activo')),
        (2,('Dañao')),
    )

    name = models.CharField(max_length=50)
    ws_type = models.IntegerField(choices=WORKSTATION_CHOICE_FIELDS, default=1)
    usb_ports = models.IntegerField(default=6, blank=True)
    red_interface = models.ForeignKey(Red_Interface, blank=True,on_delete=models.CASCADE)
    lan = models.BooleanField(default=0, blank=True)
    wlan = models.BooleanField(default=0, blank=True)
    ram = models.IntegerField(default=2048, blank=True)
    cpu = models.TextField(max_length=500, blank=True)
    hdd = models.TextField(max_length=500, blank=True)
    so = models.ForeignKey(SO,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    model = models.CharField(max_length=144, blank=True)
    version = models.CharField(max_length=144, blank=True)
    user = models.CharField(max_length=144, blank=True)
    user_pass = models.CharField(max_length=144, blank=True)
    sn = models.CharField(max_length=144, blank=True, unique=True)
    employee = models.ForeignKey(Employee, blank=True,on_delete=models.CASCADE,)
    organization = models.ForeignKey(Organization, blank=True,on_delete=models.CASCADE,)
    status = models.IntegerField(choices=STATUS_CHOICE_FIELDS, default=1)


    def __str__(self):
        return self.name

    class Meta:

        verbose_name = ('Equipment')
        verbose_name_plural = ('Equipments')
        permissions = (
            ("can_create_equipment", "Can create Equipment"),
            ("can_delete_equipment", "Can delete Equipment"),
            ("can_update_equipment", "Can update Equipment"),
        )
