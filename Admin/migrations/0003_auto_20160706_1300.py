# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_auto_20160629_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_price', models.FloatField(null=True)),
                ('total_paid', models.FloatField(null=True)),
                ('due', models.FloatField(null=True)),
                ('total_quantity', models.FloatField(null=True)),
                ('bill_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('month', models.CharField(default=b'July', max_length=100)),
                ('customer', models.ForeignKey(to='Admin.Person')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.FloatField(null=True)),
                ('price', models.FloatField(null=True)),
                ('isReturned', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='stockdetails',
            name='month',
            field=models.CharField(default=b'July', max_length=100),
        ),
        migrations.AddField(
            model_name='productslist',
            name='product',
            field=models.ForeignKey(to='Admin.StockDetails'),
        ),
        migrations.AddField(
            model_name='billing',
            name='products_list',
            field=models.ManyToManyField(to='Admin.ProductsList'),
        ),
    ]
