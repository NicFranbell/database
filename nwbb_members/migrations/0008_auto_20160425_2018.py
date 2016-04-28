# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-25 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nwbb_members', '0007_auto_20160419_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberrole',
            name='member',
        ),
        migrations.RemoveField(
            model_name='memberrole',
            name='role_type',
        ),
        migrations.AddField(
            model_name='member',
            name='bike_registration',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='member',
            name='comments',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='member',
            name='driver_license_expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='driver_license_number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='member',
            name='roles',
            field=models.ManyToManyField(blank=True, related_name='member_roles', to='nwbb_members.RoleType'),
        ),
        migrations.DeleteModel(
            name='MemberRole',
        ),
    ]
