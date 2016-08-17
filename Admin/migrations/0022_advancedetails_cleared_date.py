# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0021_advancedetails_iscleared'),
    ]

    operations = [
        migrations.AddField(
            model_name='advancedetails',
            name='cleared_date',
            field=models.DateField(default=datetime.date(2016, 8, 6)),
        ),
    ]
