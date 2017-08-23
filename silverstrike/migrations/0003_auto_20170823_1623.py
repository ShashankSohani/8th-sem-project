# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 16:23
from __future__ import unicode_literals

from django.db import migrations


def create_system_account(apps, schema_editor):
    Account = apps.get_model('silverstrike', 'Account')
    Account.objects.create(name='Sytem Account', account_type=4)


class Migration(migrations.Migration):

    dependencies = [
        ('silverstrike', '0002_auto_20170823_1617'),
    ]

    operations = [
        migrations.RunPython(create_system_account),
    ]
