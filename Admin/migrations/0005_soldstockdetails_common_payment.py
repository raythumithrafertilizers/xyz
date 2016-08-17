# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_soldstockdetails_common_advance'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldstockdetails',
            name='common_payment',
            field=models.FloatField(default=0.0),
        ),
    ]
