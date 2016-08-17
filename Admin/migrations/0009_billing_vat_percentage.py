# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_advancedetails_interest_money'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='vat_percentage',
            field=models.FloatField(default=0.0),
        ),
    ]
