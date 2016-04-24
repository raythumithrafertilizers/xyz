# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0021_auto_20160323_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_price', models.FloatField(null=True)),
                ('total_paid', models.FloatField(null=True)),
                ('due', models.FloatField(null=True)),
                ('total_quantity', models.FloatField(null=True)),
                ('bill_date', models.DateTimeField(default=datetime.datetime(2016, 3, 23, 17, 20, 22, 698161))),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=500)),
                ('last_name', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('create_date', models.DateTimeField(default=datetime.datetime(2016, 3, 23, 17, 20, 22, 697039))),
            ],
        ),
        migrations.CreateModel(
            name='ProductsList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.FloatField(null=True)),
                ('price', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='RatePerType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate_per_type_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='StockDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=500)),
                ('item_type', models.CharField(max_length=100)),
                ('item_batch_number', models.CharField(max_length=500)),
                ('item_lot_number', models.CharField(max_length=500)),
                ('expire_date', models.DateField()),
                ('mfg_date', models.DateField(null=True)),
                ('purchase_form', models.TextField()),
                ('quantity_type', models.CharField(max_length=100)),
                ('rate_per_type', models.CharField(max_length=100)),
                ('item_cost', models.FloatField(null=True)),
                ('quantity_weight', models.FloatField(null=True)),
                ('available_stock', models.FloatField(null=True)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2016, 3, 23, 17, 20, 22, 696252))),
            ],
        ),
        migrations.CreateModel(
            name='StockType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='productslist',
            name='product',
            field=models.ForeignKey(to='Admin.StockDetails'),
        ),
        migrations.AddField(
            model_name='billing',
            name='customer',
            field=models.ForeignKey(to='Admin.Customers'),
        ),
        migrations.AddField(
            model_name='billing',
            name='products_list',
            field=models.ManyToManyField(to='Admin.ProductsList'),
        ),
    ]
