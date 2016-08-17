# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0031_auto_20160807_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenditures',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]
