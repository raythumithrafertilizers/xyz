# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0009_billing_vat_percentage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billing',
            old_name='vat_percentage',
            new_name='vat',
        ),
    ]
