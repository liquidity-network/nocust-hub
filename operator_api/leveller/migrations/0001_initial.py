# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-16 11:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ledger', '0044_auto_20180930_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('beginning', models.DateTimeField(auto_now_add=True)),
                ('expiry', models.DateTimeField()),
                ('wallet', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='ledger.Wallet')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
