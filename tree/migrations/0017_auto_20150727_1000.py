# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0016_answer_пame'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='пame',
            new_name='game',
        ),
    ]
