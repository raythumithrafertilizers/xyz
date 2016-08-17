# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0026_auto_20160806_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='piadadvancedetails',
            name='paid_farmer_id',
            field=models.IntegerField(default=0),
        ),
    ]
