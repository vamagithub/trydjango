# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='pan',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
