# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-20 13:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0005_auto_20160220_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='date_of_birth',
        ),
    ]