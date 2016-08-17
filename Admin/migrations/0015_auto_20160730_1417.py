# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0014_auto_20160730_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldstockdetails',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2016, 7, 30, 14, 17, 25, 120363)),
        ),
    ]
