# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0026_auto_20160404_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockdetails',
            name='isLegal',
            field=models.CharField(default=b'legal', max_length=100),
        ),
        migrations.AlterField(
            model_name='billing',
            name='bill_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 4, 13, 52, 14, 912133)),
        ),
        migrations.AlterField(
            model_name='companybills',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 4, 13, 52, 14, 913617)),
        ),
        migrations.AlterField(
            model_name='customers',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 4, 13, 52, 14, 910977)),
        ),
        migrations.AlterField(
            model_name='stockdetails',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 4, 13, 52, 14, 910205)),
        ),
    ]
