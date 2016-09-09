# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0040_auto_20160904_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldstockdetails',
            name='stock_object',
            field=models.ForeignKey(to='Admin.StockNames', null=True),
        ),
        migrations.AlterField(
            model_name='advancedetails',
            name='paid_date',
            field=models.DateField(default=datetime.date(2016, 9, 5)),
        ),
        migrations.AlterField(
            model_name='billing',
            name='bill_date',
            field=models.DateField(default=datetime.date(2016, 9, 5)),
        ),
        migrations.AlterField(
            model_name='expenditures',
            name='create_date',
            field=models.DateField(default=datetime.date(2016, 9, 5)),
        ),
        migrations.AlterField(
            model_name='piadadvancedetails',
            name='farmer_paid_date',
            field=models.DateField(default=datetime.date(2016, 9, 5)),
        ),
        migrations.AlterField(
            model_name='soldstockdetails',
            name='created_date',
            field=models.DateField(default=datetime.date(2016, 9, 5)),
        ),
    ]
