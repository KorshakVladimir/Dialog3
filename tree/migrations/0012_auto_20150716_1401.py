# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0011_auto_20150716_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='relation_answer',
            field=models.ForeignKey(verbose_name='От какого вопроса пришел ответ', null=True, blank=True, to='tree.Answer'),
        ),
    ]
