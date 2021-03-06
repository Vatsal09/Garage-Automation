# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-24 00:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0005_remove_session_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='activesession',
            name='date_arrived',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='activesession',
            name='date_exited',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='session',
            name='date_arrived',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='session',
            name='date_exited',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
