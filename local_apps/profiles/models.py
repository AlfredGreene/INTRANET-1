from django.db import models

class Employee(models.Model):

    # user =
    name = models.CharField(max_length=50)


    def __str__(self):

        return self.name

    class Meta:

        verbose_name = ('Employee')
        verbose_name_plural = ('Employees')
        permissions = (
            ("can_create_employee", "Can create employee"),
            ("can_delete_employee", "Can delete employee"),
            ("can_update_employee", "Can update employee"),
        )
