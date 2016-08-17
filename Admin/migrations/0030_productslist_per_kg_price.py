# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0029_appendstockdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='productslist',
            name='per_kg_price',
            field=models.FloatField(default=0.0),
        ),
    ]
