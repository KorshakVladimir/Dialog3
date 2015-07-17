# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0016_remove_questions_flag_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='full_image',
            field=models.ImageField(upload_to='', null=True, blank=True, verbose_name='изображение'),
        ),
    ]
