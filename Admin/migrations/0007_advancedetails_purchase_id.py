# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_advancedetails_interest_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='advancedetails',
            name='purchase_id',
            field=models.IntegerField(default=0),
        ),
    ]
