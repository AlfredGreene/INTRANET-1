from django.db import models

from local_apps.brands.models import Brand

class Location(models.Model):

    COUNTRIES = (
        (1,('Argentina')),
        (2,('Bolivia')),
        (3,('Brasil')),
        (4,('Chile')),
        (5,('Colombia')),
        (6,('Costa Rica')),
        (7,('Cuba')),
        (8,('Ecuador')),
        (9,('El Salvador')),
        (10,('Guayana Francesa')),
        (11,('Granada')),
        (12,('Guatemala')),
        (13,('Guayana')),
        (14,('Haití')),
        (15,('Honduras')),
        (16,('Jamaica')),
        (17,('México')),
        (18,('Nicaragua')),
        (19,('Paraguay')),
        (20,('Panamá')),
        (21,('Perú')),
        (22,('Puerto Rico')),
        (23,('República Dominicana')),
        (24,('Surinam')),
        (25,('Uruguay') ),
        (26,('Venezuela')),
        (27,('Estados Unidos')),
    )

    name = models.CharField(max_length=144)
    dir1 = models.TextField(max_length=300)
    dir2 = models.TextField(max_length=300, blank=True)
    country = models.IntegerField(choices=COUNTRIES)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = ('Location')
        verbose_name_plural = ('Locations')
        permissions = (
            ("can_create_location", "Can create location"),
            ("can_delete_location", "Can delete location"),
            ("can_update_location", "Can update location"),
        )

class Organization(models.Model):

    name = models.CharField(max_length=144)
    legal_name = models.CharField(max_length=144)
    ruc = models.IntegerField( null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = ('Organization')
        verbose_name_plural = ('Organizations')
        permissions = (
            ("can_create_organization", "Can create organization"),
            ("can_delete_organization", "Can delete organization"),
            ("can_update_organization", "Can update organization"),
        )


class Store(models.Model):

    name = models.CharField(max_length=50)
    organization = models.ForeignKey(Organization)
    location = models.ForeignKey(Location)
    brand = models.ForeignKey(Brand)

    def __srt__(self):
        return self.name

    class Meta:
        verbose_name = ('Store')
        verbose_name_plural = ('Stores')
        permissions = (
            ("can_create_store", "Can create store"),
            ("can_delete_store", "Can delete store"),
            ("can_update_store", "Can update store"),
        )
