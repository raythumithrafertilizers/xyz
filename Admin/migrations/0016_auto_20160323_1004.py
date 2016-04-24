# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0015_customers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.FloatField(null=True)),
                ('payment', models.CharField(max_length=500)),
                ('customer', models.ForeignKey(to='Admin.Customers')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.FloatField(null=True)),
                ('price', models.FloatField(null=True)),
                ('product', models.ForeignKey(to='Admin.StockDetails')),
            ],
        ),
        migrations.AddField(
            model_name='billing',
            name='products_list',
            field=models.ManyToManyField(to='Admin.ProductsList'),
        ),
    ]
