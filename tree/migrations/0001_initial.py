# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('text_answer', models.CharField(verbose_name='Текст ответа', max_length=200)),
                ('depth', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Essential_prop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('value_property', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('type_prod', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image_product', models.ImageField(upload_to='', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products_property',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('value_property', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Property_char',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name_property_char', models.CharField(max_length=200)),
                ('name_property_trans', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('point_answer', models.IntegerField(verbose_name='Очки ответа', default=0)),
                ('point_emotions', models.IntegerField(verbose_name='Очки емоций', default=0)),
                ('text_questions', models.CharField(verbose_name='Текст Вопроса', max_length=200)),
                ('question_answer', models.CharField(verbose_name='Вопрос для перехода', max_length=200)),
                ('relation_answer', models.ForeignKey(verbose_name='Вопрос для связи', to='tree.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='User_rezult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('point', models.IntegerField(default=0)),
                ('session_output', models.CharField(max_length=36)),
                ('date_create', models.DateTimeField(auto_now=True)),
                ('best_choise', models.CharField(max_length=150)),
                ('answer_output', models.ForeignKey(to='tree.Answer')),
                ('product', models.ForeignKey(to='tree.Products', null=True, blank=True)),
                ('question_output', models.ForeignKey(to='tree.Questions')),
                ('user_output', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='products_property',
            name='name_property',
            field=models.ForeignKey(to='tree.Property_char'),
        ),
        migrations.AddField(
            model_name='products_property',
            name='products',
            field=models.ForeignKey(to='tree.Products'),
        ),
        migrations.AddField(
            model_name='essential_prop',
            name='name_property',
            field=models.ForeignKey(to='tree.Property_char'),
        ),
        migrations.AddField(
            model_name='essential_prop',
            name='relation_answer',
            field=models.ForeignKey(verbose_name='Вопрос для связи', to='tree.Answer'),
        ),
    ]
