# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0014_auto_20150716_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='flag_product',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
