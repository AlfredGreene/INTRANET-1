from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Documentation(models.Model):

    author = models.ForeignKey(User)
    name = models.CharField(max_length=140)
    title = models.CharField(max_length=140, blank=True)
    description = models.TextField(blank=True)
    document = models.FileField(upload_to='documents/')

    def __str__(self):

        return self.name

    class Meta:

        verbose_name = ('Documentation')
        verbose_name_plural = ('Documentation')
        permissions = (
            ("can_add_documets", "Can add documents"),
            ("can_delete_documents", "Can delete documents"),
            ("can_see_finanzas_documents", "Can see finanzas documents"),
            ("can_see_it_documents", "Can see it documents"),
        )
