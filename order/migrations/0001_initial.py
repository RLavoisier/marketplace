# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-04 22:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marketplace', models.CharField(max_length=30)),
                ('order_id', models.CharField(max_length=30)),
                ('mp_order_status', models.CharField(max_length=30)),
                ('lg_order_status', models.CharField(max_length=30)),
                ('order_amount', models.FloatField()),
                ('order_date', models.DateField(auto_now_add=True)),
                ('customer_first_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price_unit', models.FloatField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=30)),
                ('image_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='orderlines',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Products'),
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='order.OrderLines', to='order.Products'),
        ),
    ]
