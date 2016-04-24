# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0012_auto_20160320_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockdetails',
            name='quantity_weight',
            field=models.FloatField(null=True),
        ),
    ]
