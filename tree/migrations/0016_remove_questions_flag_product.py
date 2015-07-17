# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0015_questions_flag_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='flag_product',
        ),
    ]
