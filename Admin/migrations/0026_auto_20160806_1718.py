# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0025_auto_20160806_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advancedetails',
            name='cleared_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
