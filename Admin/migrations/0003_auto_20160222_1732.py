# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_auto_20160222_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stamps_wrt_bill',
            name='bill_amount',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stamps_wrt_bill',
            name='no_of_stamps',
            field=models.CharField(max_length=6),
        ),
    ]
