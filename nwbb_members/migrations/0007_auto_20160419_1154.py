# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-19 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nwbb_members', '0006_auto_20160419_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='town',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
