# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0028_auto_20160404_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='bill_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 6, 16, 35, 19, 288707)),
        ),
        migrations.AlterField(
            model_name='companybills',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 6, 16, 35, 19, 290127)),
        ),
        migrations.AlterField(
            model_name='customers',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 6, 16, 35, 19, 287577)),
        ),
        migrations.AlterField(
            model_name='stockdetails',
            name='available_stock',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='stockdetails',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 6, 16, 35, 19, 286736)),
        ),
    ]
