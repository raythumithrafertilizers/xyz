# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_auto_20160320_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockdetails',
            name='item_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stockdetails',
            name='quantity_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stockdetails',
            name='rate_per_type',
            field=models.CharField(max_length=100),
        ),
    ]
