# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_auto_20160320_1202'),
    ]

    operations = [
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
                ('item_cost', models.FloatField()),
                ('item_batch_number', models.CharField(max_length=500)),
                ('item_lot_number', models.CharField(max_length=500)),
                ('expire_date', models.DateTimeField()),
                ('mfg_date', models.DateTimeField()),
                ('purchase_form', models.TextField()),
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
            model_name='stockdetails',
            name='item_type',
            field=models.ForeignKey(to='Admin.StockType'),
        ),
        migrations.AddField(
            model_name='stockdetails',
            name='quantity_type',
            field=models.ForeignKey(to='Admin.Quantity'),
        ),
        migrations.AddField(
            model_name='stockdetails',
            name='rate_per_type',
            field=models.ForeignKey(to='Admin.RatePerType'),
        ),
    ]
