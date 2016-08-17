# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0024_auto_20160806_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='piadadvancedetails',
            old_name='paid_date',
            new_name='farmer_paid_date',
        ),
        migrations.RemoveField(
            model_name='advancedetails',
            name='farmer_paid_amount',
        ),
        migrations.RemoveField(
            model_name='advancedetails',
            name='final_total_with_interest',
        ),
        migrations.AddField(
            model_name='advancedetails',
            name='paid_details_id',
            field=models.IntegerField(default=0),
        ),
    ]
