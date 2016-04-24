# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_auto_20160222_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='store_wise_stamp_offers',
            name='store_id',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
