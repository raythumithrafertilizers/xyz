# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0037_auto_20160901_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advancedetails',
            name='paid_date',
            field=models.DateField(default=datetime.date(2016, 9, 4)),
        ),
        migrations.AlterField(
            model_name='billing',
            name='bill_date',
            field=models.DateField(default=datetime.date(2016, 9, 4)),
        ),
        migrations.AlterField(
            model_name='expenditures',
            name='create_date',
            field=models.DateField(default=datetime.date(2016, 9, 4)),
        ),
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='piadadvancedetails',
            name='farmer_paid_date',
            field=models.DateField(default=datetime.date(2016, 9, 4)),
        ),
        migrations.AlterField(
            model_name='soldstockdetails',
            name='created_date',
            field=models.DateField(default=datetime.date(2016, 9, 4)),
        ),
    ]
