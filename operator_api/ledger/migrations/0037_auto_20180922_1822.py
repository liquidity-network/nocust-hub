# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-22 18:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0036_transfer_sender_balance_marker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matching',
            name='extra_left_amount',
        ),
        migrations.RemoveField(
            model_name='matching',
            name='extra_right_amount',
        ),
    ]
