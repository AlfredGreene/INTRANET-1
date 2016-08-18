from django.db import models

# Create your models here.

class Equipment(models.Model):

    WORKSTATION_CHOICE_FIELDS = (
        (1, ('PC')),
        (2, ('LAPTOP')),
        (3, ('LAPTOP')),
        (4, ('LAPTOP')),
        (5, ('LAPTOP')),
        (6, ('LAPTOP')),
        (7, ('LAPTOP')),
        (8, ('LAPTOP')),
        (9, ('LAPTOP')),
        (10, ('LAPTOP')),
        (11, ('LAPTOP')),
        (12, ('LAPTOP')),
        (13, ('LAPTOP')),
        (14, ('LAPTOP')),
        (15, ('LAPTOP')),
    )

    name = models.CharField(max_length=50)
    ws_type = models.IntegerField(choices=WORKSTATION_CHOICE_FIELDS, default=1)

    def __str__(self):

        return self.name

    class Meta:

        verbose_name = ('Equipment')
        verbose_name_plural = ('Equipments')
        permissions = (
            ("can_create_workstation", "Can create workstation"),
            ("can_delete_workstation", "Can delete workstation"),
            ("can_update_workstation", "Can update workstation"),
        )
