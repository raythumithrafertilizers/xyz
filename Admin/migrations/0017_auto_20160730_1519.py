# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0016_auto_20160730_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='advancedetails',
            name='remarks',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='advancedetails',
            name='paid_date',
            field=models.DateTimeField(default=datetime.date(2016, 7, 30)),
        ),
    ]
