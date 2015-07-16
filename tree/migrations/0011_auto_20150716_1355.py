# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0010_auto_20150715_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='relation_answer',
            field=models.ForeignKey(to='tree.Answer', blank=True, verbose_name='От какого вопроса пришел ответ'),
        ),
    ]
