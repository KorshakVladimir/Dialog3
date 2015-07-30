# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0014_game'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Game',
        ),
    ]
