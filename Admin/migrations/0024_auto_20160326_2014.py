# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0023_auto_20160323_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='productslist',
            name='isReturned',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='billing',
            name='bill_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 26, 20, 14, 57, 850745)),
        ),
        migrations.AlterField(
            model_name='customers',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 26, 20, 14, 57, 849664)),
        ),
        migrations.AlterField(
            model_name='stockdetails',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 26, 20, 14, 57, 848976)),
        ),
    ]
