# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_soldstockdetails_common_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='advancedetails',
            name='interest_rate',
            field=models.FloatField(default=0.0),
        ),
    ]
