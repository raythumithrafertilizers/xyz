# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0033_auto_20160814_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='remarks',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='billing',
            name='vehicle_number',
            field=models.TextField(default=b''),
        ),
    ]
