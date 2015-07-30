# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0013_auto_20150720_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(verbose_name='Имя', max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Игры',
                'verbose_name': 'Игра',
            },
        ),
    ]
