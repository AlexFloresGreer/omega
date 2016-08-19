# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omega', '0003_travel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='end_date',
            field=models.DateTimeField(verbose_name=['%m-%d-%Y']),
        ),
        migrations.AlterField(
            model_name='travel',
            name='start_date',
            field=models.DateTimeField(verbose_name=['%m-%d-%Y']),
        ),
    ]
