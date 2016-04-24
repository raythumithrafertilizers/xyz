# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0013_stockdetails_quantity_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockdetails',
            name='available_stock',
            field=models.FloatField(null=True),
        ),
    ]
