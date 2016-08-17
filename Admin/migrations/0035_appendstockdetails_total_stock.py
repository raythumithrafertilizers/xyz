# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0034_auto_20160814_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='appendstockdetails',
            name='total_stock',
            field=models.FloatField(default=0.0),
        ),
    ]
