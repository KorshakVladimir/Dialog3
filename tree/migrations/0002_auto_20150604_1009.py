# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relations_tying_products',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('product', models.ForeignKey(to='tree.Products')),
            ],
        ),
        migrations.CreateModel(
            name='Tying_products',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='relations_tying_products',
            name='tying_product',
            field=models.ForeignKey(to='tree.Tying_products'),
        ),
    ]
