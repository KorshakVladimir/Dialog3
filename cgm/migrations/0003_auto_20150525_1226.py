# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cgm', '0002_remove_userprofile_bio1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(null=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, blank=True),
        ),
    ]
