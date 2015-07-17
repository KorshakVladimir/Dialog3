# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0008_auto_20150701_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='full_image',
            field=models.ImageField(blank=True, upload_to='', null=True, verbose_name='изображение'),
        ),
    ]
