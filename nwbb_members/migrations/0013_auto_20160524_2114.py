# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-24 20:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nwbb_members', '0012_auto_20160522_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberTraining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_completed', models.DateField(blank=True)),
                ('expiry_date', models.DateField(blank=True)),
                ('awarded_by', models.CharField(blank=True, max_length=200)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_training', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='membertraining',
            name='training',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_training', to='nwbb_members.Training'),
        ),
    ]