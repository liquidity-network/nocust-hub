# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-29 14:55
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0002_pgsql_constraints'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='registration_round',
            field=models.BigIntegerField(
                validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
