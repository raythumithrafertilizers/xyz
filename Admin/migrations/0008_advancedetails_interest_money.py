# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_advancedetails_purchase_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='advancedetails',
            name='interest_money',
            field=models.FloatField(default=0.0),
        ),
    ]
