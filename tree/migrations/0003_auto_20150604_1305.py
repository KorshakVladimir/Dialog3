# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0002_auto_20150604_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_rezult',
            name='product',
        ),
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_rezult',
            name='money',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_rezult',
            name='type_quest',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user_rezult',
            name='answer_output',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user_rezult',
            name='question_output',
            field=models.CharField(max_length=200),
        ),
    ]
