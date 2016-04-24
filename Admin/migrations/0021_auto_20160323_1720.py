# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0020_auto_20160323_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billing',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='billing',
            name='products_list',
        ),
        migrations.RemoveField(
            model_name='productslist',
            name='product',
        ),
        migrations.DeleteModel(
            name='Quantity',
        ),
        migrations.DeleteModel(
            name='RatePerType',
        ),
        migrations.DeleteModel(
            name='StockType',
        ),
        migrations.DeleteModel(
            name='Billing',
        ),
        migrations.DeleteModel(
            name='Customers',
        ),
        migrations.DeleteModel(
            name='ProductsList',
        ),
        migrations.DeleteModel(
            name='StockDetails',
        ),
    ]
