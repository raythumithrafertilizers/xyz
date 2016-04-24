# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0017_billing_bill_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 23, 15, 32, 26, 461823)),
        ),
        migrations.AddField(
            model_name='stockdetails',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 23, 15, 32, 26, 461102)),
        ),
        migrations.AlterField(
            model_name='billing',
            name='bill_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 23, 15, 32, 26, 462904)),
        ),
    ]
