# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0043_auto_20160905_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldstockdetails',
            name='stock_object',
            field=models.ForeignKey(default=b'', to='Admin.StockNames', null=True),
        ),
    ]
