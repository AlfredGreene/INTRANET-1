from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='brands_logo', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('Brand')
        verbose_name_plural = ('Brands')
        permissions = (
            ("can_create_brand", "Can create brand"),
            ("can_delete_brand", "Can delete brand"),
            ("can_update_brand", "Can update brand"),
        )
