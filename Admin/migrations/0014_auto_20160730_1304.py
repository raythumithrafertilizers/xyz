# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0013_soldstockdetails_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldstockdetails',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 30, 13, 4, 1, 211157)),
        ),
    ]
