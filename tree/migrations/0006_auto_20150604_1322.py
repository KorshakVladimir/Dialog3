# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0005_auto_20150604_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_rezult',
            name='answer_text',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user_rezult',
            name='answer_output',
            field=models.ForeignKey(null=True, to='tree.Answer', blank=True),
        ),
    ]
