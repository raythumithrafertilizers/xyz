# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('token', models.CharField(unique=True, max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('token_type', models.IntegerField(default=1)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=25)),
                ('activationCode', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=15)),
                ('membershipType', models.CharField(max_length=10)),
                ('totalStamps', models.IntegerField(default=0)),
                ('currentStamps', models.IntegerField(default=0)),
                ('userKey', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
