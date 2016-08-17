# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0022_advancedetails_cleared_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='paid_advance_details',
            field=models.ManyToManyField(to='Admin.PiadAdvanceDetails'),
        ),
    ]
