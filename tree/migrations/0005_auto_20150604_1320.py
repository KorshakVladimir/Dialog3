# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0004_tying_products_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_rezult',
            name='answer_output',
            field=models.ForeignKey(to='tree.Answer'),
        ),
    ]
