# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0016_auto_20160323_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='bill_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 23, 15, 30, 54, 4338)),
        ),
    ]
