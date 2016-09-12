# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0047_auto_20160911_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='soldstockdetails',
            old_name='quantity_in_tons',
            new_name='quantity_in_numbers',
        ),
    ]
