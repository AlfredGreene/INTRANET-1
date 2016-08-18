# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=144)),
                ('legal_name', models.CharField(max_length=144)),
                ('ruc', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'permissions': (('can_create_organization', 'Can create organization'), ('can_delete_organization', 'Can delete organization'), ('can_update_organization', 'Can update organization')),
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organizations',
            },
        ),
    ]
