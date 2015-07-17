# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0009_auto_20150714_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='point_answer',
            field=models.IntegerField(verbose_name='Очки ответа', blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='questions',
            name='point_emotions',
            field=models.IntegerField(verbose_name='Очки емоций', blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question_answer',
            field=models.CharField(verbose_name='К какому вопросу приведет ответ', blank=True, max_length=200),
        ),
    ]
