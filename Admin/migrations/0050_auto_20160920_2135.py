# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0049_auto_20160914_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advancedetails',
            name='paid_date',
            field=models.DateField(default=datetime.date(2016, 9, 20)),
        ),
        migrations.AlterField(
            model_name='billing',
            name='bill_date',
            field=models.DateField(default=datetime.date(2016, 9, 20)),
        ),
        migrations.AlterField(
            model_name='expenditures',
            name='create_date',
            field=models.DateField(default=datetime.date(2016, 9, 20)),
        ),
        migrations.AlterField(
            model_name='piadadvancedetails',
            name='farmer_paid_date',
            field=models.DateField(default=datetime.date(2016, 9, 20)),
        ),
        migrations.AlterField(
            model_name='soldstockdetails',
            name='created_date',
            field=models.DateField(default=datetime.date(2016, 9, 20)),
        ),
    ]
