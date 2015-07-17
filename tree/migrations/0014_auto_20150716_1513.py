# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0013_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='full_image',
        ),
        migrations.AlterField(
            model_name='questions',
            name='question_answer',
            field=models.CharField(blank=True, verbose_name='К какому вопросу приведет ответ', max_length=200),
        ),
        migrations.AlterField(
            model_name='questions',
            name='relation_answer',
            field=models.ForeignKey(null=True, blank=True, to='tree.Answer', verbose_name='От какого вопроса пришел ответ'),
        ),
    ]
