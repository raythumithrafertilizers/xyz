# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0041_auto_20160905_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldstockdetails',
            name='farmer',
            field=models.ForeignKey(related_name='farmer_data', default=b'', to='Admin.Person'),
        ),
        migrations.AlterField(
            model_name='soldstockdetails',
            name='harvester',
            field=models.ForeignKey(related_name='harvester_data', default=b'', to='Admin.Person'),
        ),
    ]
