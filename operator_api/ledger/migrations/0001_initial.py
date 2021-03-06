# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-29 11:49
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aggregate',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_spendings', models.DecimalField(decimal_places=0, max_digits=80,
                                                          validators=[django.core.validators.MinValueValidator(Decimal('0'))])),
                ('updated_gains', models.DecimalField(blank=True, decimal_places=0, max_digits=80,
                                                      null=True, validators=[django.core.validators.MinValueValidator(Decimal('0'))])),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('round', models.BigIntegerField()),
                ('tx_set_hash', models.CharField(max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('round', models.BigIntegerField()),
                ('left', models.DecimalField(decimal_places=0, max_digits=80, validators=[
                 django.core.validators.MinValueValidator(Decimal('0'))])),
                ('right', models.DecimalField(decimal_places=0, max_digits=80, validators=[
                 django.core.validators.MinValueValidator(Decimal('0'))])),
                ('merkle_proof_hashes', models.CharField(
                    blank=True, max_length=2048)),
                ('merkle_proof_values', models.CharField(blank=True, max_length=2592, validators=[django.core.validators.RegexValidator(
                    re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')])),
                ('merkle_proof_trail', models.DecimalField(decimal_places=0, max_digits=60,
                                                           validators=[django.core.validators.MinValueValidator(Decimal('0'))])),
                ('merkle_proof_aggregate', models.ForeignKey(blank=True, null=True,
                                                             on_delete=django.db.models.deletion.PROTECT, to='ledger.Aggregate')),
            ],
        ),
        migrations.CreateModel(
            name='BlockchainTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('txid', models.CharField(max_length=256)),
                ('block', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Checkpoint',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('round', models.BigIntegerField()),
                ('merkle_root', models.CharField(max_length=64)),
                ('block', models.BigIntegerField()),
                ('upper_bound', models.DecimalField(decimal_places=0, max_digits=80, validators=[
                 django.core.validators.MinValueValidator(Decimal('0'))])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=0, max_digits=80, validators=[
                 django.core.validators.MinValueValidator(Decimal('0'))])),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('round', models.BigIntegerField()),
                ('block', models.BigIntegerField()),
                ('balance', models.ForeignKey(blank=True, null=True,
                                              on_delete=django.db.models.deletion.PROTECT, to='ledger.Balance')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('checksum', models.CharField(max_length=64)),
                ('value', models.CharField(max_length=130)),
                ('data', models.CharField(blank=True, max_length=4096, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('block', models.BigIntegerField(unique=True)),
                ('round', models.BigIntegerField()),
                ('last_checkpoint_submission_round', models.BigIntegerField()),
                ('pending_withdrawals', models.DecimalField(decimal_places=0, max_digits=80,
                                                            validators=[django.core.validators.MinValueValidator(Decimal('0'))])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=0, max_digits=80, validators=[
                 django.core.validators.MinValueValidator(Decimal('0'))])),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('round', models.BigIntegerField()),
                ('nonce', models.DecimalField(blank=True, decimal_places=0, max_digits=80,
                                              null=True, validators=[django.core.validators.MinValueValidator(Decimal('0'))])),
                ('processed', models.BooleanField(default=False)),
                ('sent', models.BooleanField(default=False)),
                ('balance', models.ForeignKey(blank=True, null=True,
                                              on_delete=django.db.models.deletion.PROTECT, to='ledger.Balance')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=40)),
                ('registration_round', models.BigIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=0, max_digits=80, validators=[
                 django.core.validators.MinValueValidator(Decimal('0'))])),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('round', models.BigIntegerField()),
                ('block', models.BigIntegerField()),
                ('balance', models.ForeignKey(blank=True, null=True,
                                              on_delete=django.db.models.deletion.PROTECT, to='ledger.Balance')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WithdrawalRequest',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=0, max_digits=80, validators=[
                 django.core.validators.MinValueValidator(Decimal('0'))])),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('round', models.BigIntegerField()),
                ('highest_spendings', models.DecimalField(decimal_places=0, max_digits=80,
                                                          validators=[django.core.validators.MinValueValidator(Decimal('0'))])),
                ('block', models.BigIntegerField()),
                ('balance', models.ForeignKey(blank=True, null=True,
                                              on_delete=django.db.models.deletion.PROTECT, to='ledger.Balance')),
                ('wallet', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='ledger.Wallet')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CheckpointSubmission',
            fields=[
                ('blockchaintransaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                                                                   parent_link=True, primary_key=True, serialize=False, to='ledger.BlockchainTransaction')),
                ('checkpoint', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='ledger.Checkpoint')),
            ],
            options={
                'abstract': False,
            },
            bases=('ledger.blockchaintransaction',),
        ),
        migrations.AddField(
            model_name='withdrawal',
            name='request',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to='ledger.WithdrawalRequest'),
        ),
        migrations.AddField(
            model_name='withdrawal',
            name='wallet',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to='ledger.Wallet'),
        ),
        migrations.AddField(
            model_name='transfer',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                    related_name='transfer_recipient_wallet', to='ledger.Wallet'),
        ),
        migrations.AddField(
            model_name='transfer',
            name='recipient_aggregate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    related_name='transfer_recipient_aggregate', to='ledger.Aggregate'),
        ),
        migrations.AddField(
            model_name='transfer',
            name='sender_aggregate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                    related_name='transfer_sender_aggregate', to='ledger.Aggregate'),
        ),
        migrations.AddField(
            model_name='transfer',
            name='wallet',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to='ledger.Wallet'),
        ),
        migrations.AddField(
            model_name='signature',
            name='wallet',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to='ledger.Wallet'),
        ),
        migrations.AddField(
            model_name='deposit',
            name='wallet',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to='ledger.Wallet'),
        ),
        migrations.AddField(
            model_name='balance',
            name='wallet',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to='ledger.Wallet'),
        ),
        migrations.AddField(
            model_name='aggregate',
            name='hub_signature',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    related_name='aggregate_hub_signature', to='ledger.Signature'),
        ),
        migrations.AddField(
            model_name='aggregate',
            name='wallet',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to='ledger.Wallet'),
        ),
        migrations.AddField(
            model_name='aggregate',
            name='wallet_signature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                    related_name='aggregate_wallet_signature', to='ledger.Signature'),
        ),
        migrations.AlterUniqueTogether(
            name='balance',
            unique_together=set([('wallet', 'round')]),
        ),
    ]
