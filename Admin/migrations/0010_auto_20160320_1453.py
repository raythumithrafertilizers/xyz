# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0009_auto_20160320_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockdetails',
            name='expire_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='stockdetails',
            name='mfg_date',
            field=models.DateField(),
        ),
    ]
