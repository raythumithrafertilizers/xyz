# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0011_auto_20160320_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockdetails',
            name='mfg_date',
            field=models.DateField(null=True),
        ),
    ]
