# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0012_auto_20150716_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='media_file',
            field=models.FileField(upload_to='Answer_media', blank=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='media_file',
            field=models.FileField(upload_to='Questions_media', blank=True),
        ),
    ]
