# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0031_auto_20160407_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockdetails',
            name='seen',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='billing',
            name='bill_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 7, 13, 37, 18, 379883)),
        ),
        migrations.AlterField(
            model_name='companybills',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 7, 13, 37, 18, 381576)),
        ),
        migrations.AlterField(
            model_name='customers',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 7, 13, 37, 18, 378555)),
        ),
        migrations.AlterField(
            model_name='galleryimages',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 7, 13, 37, 18, 382089)),
        ),
        migrations.AlterField(
            model_name='stockdetails',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 7, 13, 37, 18, 377676)),
        ),
    ]
