# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 22:46
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0012_session_creditcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking_lot',
            name='max_levels',
            field=models.CharField(max_length=3, validators=[django.core.validators.RegexValidator('^[1-9]\\d{0,2}$')]),
        ),
        migrations.AlterField(
            model_name='parking_lot',
            name='max_spots',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('^[1-9]\\d{0,4}$')]),
        ),
    ]
