# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-05 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20170705_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='lg_order_status',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='mp_order_status',
            field=models.CharField(max_length=30),
        ),
    ]
