from django.db import models


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
