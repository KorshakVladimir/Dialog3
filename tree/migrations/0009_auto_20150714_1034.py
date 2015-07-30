# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0008_auto_20150703_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='Имя', max_length=150)),
            ],
            options={
                'verbose_name': 'Этап диалога',
                'verbose_name_plural': 'Этапы диалогов',
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='stage',
            field=models.ForeignKey(verbose_name='Этап диалога', null=True, blank=True, to='tree.Stages'),
        ),
    ]
