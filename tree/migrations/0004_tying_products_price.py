# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0003_auto_20150604_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='tying_products',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
