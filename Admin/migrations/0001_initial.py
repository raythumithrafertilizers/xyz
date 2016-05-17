# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
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
                ('bill_date', models.DateTimeField(default=datetime.datetime(2016, 5, 17, 20, 21, 17, 436412))),
                ('description', models.TextField()),
                ('month', models.CharField(default=b'May', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyBills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=300)),
                ('company_invoice_number', models.CharField(max_length=300)),
                ('company_tin_number', models.CharField(default=b'', max_length=300)),
                ('bill_image', models.FileField(upload_to=b'static/static/uploads/')),
                ('invoice_date', models.DateField(verbose_name=datetime.date(2016, 5, 17))),
                ('uploaded_at', models.DateTimeField(default=datetime.datetime(2016, 5, 17, 20, 21, 17, 430655))),
            ],
        ),
        migrations.CreateModel(
            name='CustomerPayments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('paid_amount', models.FloatField(default=0.0)),
                ('paid_date', models.DateField(default=datetime.date(2016, 5, 17))),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=500)),
                ('last_name', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('create_date', models.DateTimeField(default=datetime.datetime(2016, 5, 17, 20, 21, 17, 433728))),
                ('customer_payments', models.ManyToManyField(to='Admin.CustomerPayments')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gallery_image', models.FileField(upload_to=b'static/static/upload_gallary_images/')),
                ('uploaded_at', models.DateTimeField(default=datetime.datetime(2016, 5, 17, 20, 21, 17, 438180))),
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
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='RatePerType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate_per_type_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='StockDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=500)),
                ('item_type', models.CharField(max_length=100)),
                ('item_batch_number', models.CharField(max_length=500)),
                ('item_lot_number', models.CharField(max_length=500)),
                ('expire_date', models.DateField()),
                ('mfg_date', models.DateField(null=True)),
                ('purchase_form', models.TextField()),
                ('quantity_type', models.CharField(max_length=100)),
                ('rate_per_type', models.CharField(max_length=100)),
                ('invoice_cost', models.FloatField(null=True)),
                ('item_cost', models.FloatField(null=True)),
                ('quantity_weight', models.FloatField(null=True)),
                ('available_stock', models.FloatField(default=0.0)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2016, 5, 17, 20, 21, 17, 431732))),
                ('isLegal', models.CharField(default=b'legal', max_length=100)),
                ('month', models.CharField(default=b'May', max_length=100)),
                ('seen', models.BooleanField(default=False)),
                ('invoice_bill', models.ForeignKey(blank=True, to='Admin.CompanyBills', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='productslist',
            name='product',
            field=models.ForeignKey(to='Admin.StockDetails'),
        ),
        migrations.AddField(
            model_name='billing',
            name='customer',
            field=models.ForeignKey(to='Admin.Customers'),
        ),
        migrations.AddField(
            model_name='billing',
            name='products_list',
            field=models.ManyToManyField(to='Admin.ProductsList'),
        ),
    ]
