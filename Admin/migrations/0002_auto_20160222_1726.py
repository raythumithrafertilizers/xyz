# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stamps_wrt_bill',
            name='no_of_stamps',
            field=models.CharField(max_length=5),
        ),
    ]
