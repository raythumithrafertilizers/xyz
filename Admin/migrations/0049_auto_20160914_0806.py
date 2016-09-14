# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0048_auto_20160911_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='appendstockdetails',
            name='manual_create_or_append_stock_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='advancedetails',
            name='paid_date',
            field=models.DateField(default=datetime.date(2016, 9, 14)),
        ),
        migrations.AlterField(
            model_name='billing',
            name='bill_date',
            field=models.DateField(default=datetime.date(2016, 9, 14)),
        ),
        migrations.AlterField(
            model_name='expenditures',
            name='create_date',
            field=models.DateField(default=datetime.date(2016, 9, 14)),
        ),
        migrations.AlterField(
            model_name='piadadvancedetails',
            name='farmer_paid_date',
            field=models.DateField(default=datetime.date(2016, 9, 14)),
        ),
        migrations.AlterField(
            model_name='soldstockdetails',
            name='created_date',
            field=models.DateField(default=datetime.date(2016, 9, 14)),
        ),
    ]
