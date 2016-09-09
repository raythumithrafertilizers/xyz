# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0039_auto_20160904_1053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='soldstockdetails',
            name='farmer_advance',
        ),
        migrations.RemoveField(
            model_name='soldstockdetails',
            name='harvester_advance',
        ),
    ]
