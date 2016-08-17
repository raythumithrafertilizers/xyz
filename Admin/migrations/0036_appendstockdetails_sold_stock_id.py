# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0035_appendstockdetails_total_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='appendstockdetails',
            name='sold_stock_id',
            field=models.IntegerField(default=0),
        ),
    ]
