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
            options={'verbose_name': 'Ответ пользователя', 'verbose_name_plural': 'Ответы пользователя'},
        ),
        migrations.AlterModelOptions(
            name='essential_prop',
            options={'verbose_name': 'Свойство вопросов', 'verbose_name_plural': 'Свойства вопросов'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterModelOptions(
            name='products_property',
            options={'verbose_name': 'Значение свойств', 'verbose_name_plural': 'Значений свойств'},
        ),
        migrations.AlterModelOptions(
            name='property_char',
            options={'verbose_name': 'Название свойства', 'verbose_name_plural': 'Название свойств'},
        ),
        migrations.AlterModelOptions(
            name='questions',
            options={'verbose_name': 'Ответ консультанта', 'verbose_name_plural': 'Ответы консультанта'},
        ),
        migrations.AlterModelOptions(
            name='relations_tying_products',
            options={'verbose_name': 'Сопутствующий товар для основного товара', 'verbose_name_plural': 'Сопутствующие товары для основного товара'},
        ),
        migrations.AlterModelOptions(
            name='tying_products',
            options={'verbose_name': 'Сопутствующий товар', 'verbose_name_plural': 'Сопутствующие товары'},
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
            field=models.CharField(verbose_name='Имя', max_length=200),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(verbose_name='Цена', default=0),
        ),
        migrations.AlterField(
            model_name='products',
            name='type_prod',
            field=models.CharField(verbose_name='тип', max_length=200),
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
            field=models.CharField(verbose_name='Значение', max_length=200),
        ),
        migrations.AlterField(
            model_name='property_char',
            name='name_property_char',
            field=models.CharField(verbose_name='Свойства латиница', max_length=200),
        ),
        migrations.AlterField(
            model_name='property_char',
            name='name_property_trans',
            field=models.CharField(verbose_name='Свойства кирилица', max_length=200),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question_answer',
            field=models.CharField(verbose_name='К какому вопросу приведет ответ', max_length=200),
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
            field=models.CharField(verbose_name='Имя', max_length=150),
        ),
        migrations.AlterField(
            model_name='tying_products',
            name='price',
            field=models.IntegerField(verbose_name='Цена', default=0),
        ),
    ]
