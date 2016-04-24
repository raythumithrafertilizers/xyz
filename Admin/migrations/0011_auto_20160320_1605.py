# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0010_auto_20160320_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockdetails',
            name='item_cost',
            field=models.FloatField(null=True),
        ),
    ]
