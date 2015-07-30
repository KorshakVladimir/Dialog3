# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game_control', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='location',
            field=models.ImageField(upload_to='', null=True, verbose_name='Фон', blank=True),
        ),
        migrations.AddField(
            model_name='game',
            name='person',
            field=models.ImageField(upload_to='', null=True, verbose_name='персонаж', blank=True),
        ),
    ]
