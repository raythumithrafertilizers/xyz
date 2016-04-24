# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0025_auto_20160402_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='month',
            field=models.CharField(default=b'April', max_length=100),
        ),
        migrations.AlterField(
            model_name='billing',
            name='bill_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 4, 11, 59, 12, 347447)),
        ),
        migrations.AlterField(
            model_name='companybills',
            name='bill_image',
            field=models.FileField(upload_to=b'static/static/uploads/'),
        ),
        migrations.AlterField(
            model_name='companybills',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 4, 11, 59, 12, 349222)),
        ),
        migrations.AlterField(
            model_name='customers',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 4, 11, 59, 12, 346275)),
        ),
        migrations.AlterField(
            model_name='stockdetails',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 4, 11, 59, 12, 345251)),
        ),
    ]
