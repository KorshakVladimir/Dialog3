# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game_control', '0001_initial'),
        ('tree', '0015_delete_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='пame',
            field=models.ForeignKey(verbose_name='Игра', blank=True, to='game_control.Game', null=True),
        ),
    ]
