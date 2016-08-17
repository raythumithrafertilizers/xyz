# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0010_auto_20160730_0937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billing',
            old_name='vat',
            new_name='vat_money',
        ),
        migrations.AddField(
            model_name='billing',
            name='vat_percentage',
            field=models.FloatField(default=0.0),
        ),
    ]
