# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0011_auto_20160730_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='remarks',
            field=models.TextField(default=b''),
        ),
    ]
