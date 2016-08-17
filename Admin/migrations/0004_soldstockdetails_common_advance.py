# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_auto_20160706_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldstockdetails',
            name='common_advance',
            field=models.FloatField(default=0.0),
        ),
    ]
