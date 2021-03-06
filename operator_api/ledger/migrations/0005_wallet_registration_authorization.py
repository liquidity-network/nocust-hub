# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-30 10:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0004_auto_20171230_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='registration_authorization',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT,
                                    related_name='wallet_registration_signature', to='ledger.Signature'),
            preserve_default=False,
        ),
    ]
