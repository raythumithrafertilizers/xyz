# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0020_auto_20160806_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='advancedetails',
            name='isCleared',
            field=models.BooleanField(default=False),
        ),
    ]
