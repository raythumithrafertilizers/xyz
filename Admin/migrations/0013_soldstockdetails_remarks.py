# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0012_billing_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldstockdetails',
            name='remarks',
            field=models.TextField(default=b''),
        ),
    ]
