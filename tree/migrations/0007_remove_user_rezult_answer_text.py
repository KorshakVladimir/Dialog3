# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0006_auto_20150604_1322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_rezult',
            name='answer_text',
        ),
    ]
