# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omega', '0002_travel_travelmanager'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='description',
            field=models.CharField(max_length=45, null=True),
        ),
    ]