# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0027_piadadvancedetails_paid_farmer_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='soldstockdetails',
            old_name='common_advance',
            new_name='miscellaneous_detections',
        ),
        migrations.RemoveField(
            model_name='soldstockdetails',
            name='common_payment',
        ),
    ]
