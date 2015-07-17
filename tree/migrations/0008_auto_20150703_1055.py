# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0007_remove_user_rezult_answer_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name_plural': 'Ответы пользователя', 'verbose_name': 'Ответ пользователя'},
        ),
        migrations.AlterModelOptions(
            name='essential_prop',
            options={'verbose_name_plural': 'Свойства вопросов', 'verbose_name': 'Свойство вопросов'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'Продукты', 'verbose_name': 'Продукт'},
        ),
        migrations.AlterModelOptions(
            name='products_property',
            options={'verbose_name_plural': 'Значений свойств', 'verbose_name': 'Значение свойств'},
        ),
        migrations.AlterModelOptions(
            name='property_char',
            options={'verbose_name_plural': 'Название свойств', 'verbose_name': 'Название свойства'},
        ),
        migrations.AlterModelOptions(
            name='questions',
            options={'verbose_name_plural': 'Ответы консультанта', 'verbose_name': 'Ответ консультанта'},
        ),
        migrations.AlterModelOptions(
            name='relations_tying_products',
            options={'verbose_name_plural': 'Сопутствующие товары для основного товара', 'verbose_name': 'Сопутствующий товар для основного товара'},
        ),
        migrations.AlterModelOptions(
            name='tying_products',
            options={'verbose_name_plural': 'Сопутствующие товары', 'verbose_name': 'Сопутствующий товар'},
        ),
        migrations.AlterField(
            model_name='answer',
            name='text_answer',
            field=models.CharField(blank=True, max_length=200, verbose_name='Текст ответа'),
        ),
        migrations.AlterField(
            model_name='essential_prop',
            name='relation_answer',
            field=models.ForeignKey(verbose_name='Вопрос', to='tree.Answer'),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image_product',
            field=models.ImageField(blank=True, upload_to='', verbose_name='изображение', null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='products',
            name='type_prod',
            field=models.CharField(max_length=200, verbose_name='тип'),
        ),
        migrations.AlterField(
            model_name='products_property',
            name='name_property',
            field=models.ForeignKey(verbose_name='Имя', to='tree.Property_char'),
        ),
        migrations.AlterField(
            model_name='products_property',
            name='products',
            field=models.ForeignKey(verbose_name='Продукт', to='tree.Products'),
        ),
        migrations.AlterField(
            model_name='products_property',
            name='value_property',
            field=models.CharField(max_length=200, verbose_name='Значение'),
        ),
        migrations.AlterField(
            model_name='property_char',
            name='name_property_char',
            field=models.CharField(max_length=200, verbose_name='Свойства латиница'),
        ),
        migrations.AlterField(
            model_name='property_char',
            name='name_property_trans',
            field=models.CharField(max_length=200, verbose_name='Свойства кирилица'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question_answer',
            field=models.CharField(max_length=200, verbose_name='К какому вопросу приведет ответ'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='relation_answer',
            field=models.ForeignKey(verbose_name='От какого вопроса пришел ответ', to='tree.Answer'),
        ),
        migrations.AlterField(
            model_name='relations_tying_products',
            name='product',
            field=models.ForeignKey(verbose_name='Товар', to='tree.Products'),
        ),
        migrations.AlterField(
            model_name='relations_tying_products',
            name='tying_product',
            field=models.ForeignKey(verbose_name='Сопутствующий товар', to='tree.Tying_products'),
        ),
        migrations.AlterField(
            model_name='tying_products',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='tying_products',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
    ]
