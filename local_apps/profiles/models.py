import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ProfileType(models.Model):

    name =  models.CharField(max_length=50)

    def __str__(self):

        return self.name

    class Meta:

        verbose_name = ('Profile')
        verbose_name_plural = ('Profiles')
        permissions = (
            ("can_create_profile", "Can create profile"),
            ("can_delete_profile", "Can delete profile"),
            ("can_update_profile", "Can update profile"),
            ("is_office_user", "Is an user from the office"),
            ("is_office_provider", "Is an office provider"),
            ("is_store_user", "Is an user from an store"),
            ("is_store_provider", "Is an provider"),
        )



class Employee(models.Model):

    GENRE_CHOICE = (
        (1,('Hombre')),
        (2,('Mujer')),
    )

    intra_user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(max_length=200, blank=True)
    genre = models.IntegerField(choices=GENRE_CHOICE,default=1)
    profiletype = models.ForeignKey(ProfileType,on_delete=models.CASCADE,)
    avatar = models.ImageField(upload_to="user_profile_avatar",blank=True)

    def __str__(self):

        return self.user_name()

    def user_name(self):
        return '%s %s' % (self.first_name,self.last_name)

    class Meta:

        verbose_name = ('Employee')
        verbose_name_plural = ('Employees')
        permissions = (
            ("can_create_employee", "Can create employee"),
            ("can_delete_employee", "Can delete employee"),
            ("can_update_employee", "Can update employee"),
        )
