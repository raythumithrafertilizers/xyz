# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0028_auto_20160806_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppendStockDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateField(null=True)),
                ('append_count', models.FloatField(default=0.0)),
                ('remarks', models.TextField()),
                ('stock', models.ForeignKey(to='Admin.StockDetails')),
            ],
        ),
    ]
