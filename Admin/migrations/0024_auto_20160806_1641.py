# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0023_person_paid_advance_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='paid_advance_details',
        ),
        migrations.AddField(
            model_name='advancedetails',
            name='farmer_paid_amount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='advancedetails',
            name='final_total_with_interest',
            field=models.FloatField(default=0.0),
        ),
    ]
