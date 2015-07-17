
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Stages(models.Model):
    name = models.CharField(max_length=150,verbose_name=u'Имя')
    class Meta:
        verbose_name = "Этап диалога"
        verbose_name_plural = "Этапы диалогов"

    def __str__(self):
        return self.name



class Answer(models.Model):

    stage = models.ForeignKey(
        Stages, verbose_name = u'Этап диалога', blank = True, null = True)

    text_answer = models.CharField(
        max_length=200, verbose_name = u'Текст ответа', blank = True)

    depth = models.IntegerField(default = 0)

    class Meta:
        verbose_name = "Ответ пользователя"
        verbose_name_plural = "Ответы пользователя"

    def __unicode__(self):
        return self.text_answer

    def __str__(self):
        return self.text_answer


class Questions(models.Model):
    point_answer = models.IntegerField(default=0, verbose_name=u'Очки ответа',blank = True)
    point_emotions = models.IntegerField(
        default=0, verbose_name=u'Очки емоций', blank = True)

    text_questions = models.CharField(
        max_length=200, verbose_name=u'Текст Вопроса')
    
    relation_answer = models.ForeignKey(
        Answer, verbose_name=u'От какого вопроса пришел ответ', blank = True,null = True)

    question_answer = models.CharField(
        verbose_name=u'К какому вопросу приведет ответ', max_length = 200, blank = True)

    class Meta:
        verbose_name = "Ответ консультанта"
        verbose_name_plural = "Ответы консультанта"

    def __unicode__(self):
        return self.text_questions

    def __str__(self):
        return self.text_questions


class Property_char(models.Model):
    name_property_char = models.CharField(max_length=200, verbose_name=u'Свойства латиница')
    name_property_trans = models.CharField(max_length=200,verbose_name=u'Свойства кирилица')

    class Meta:
        verbose_name = "Название свойства"
        verbose_name_plural = "Название свойств"

    def __str__(self):
        return self.name_property_char


class Products(models.Model):
    name = models.CharField(max_length=200,verbose_name=u'Имя')
    type_prod = models.CharField(max_length=200,verbose_name=u'тип')
    description = models.TextField(verbose_name=u'Описание')
    price = models.IntegerField(default=0,verbose_name=u'Цена')
    image_product = models.ImageField(blank=True, null=True,verbose_name=u'изображение')

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name


class Products_property(models.Model):
    products = models.ForeignKey(Products, verbose_name=u'Продукт')
    name_property = models.ForeignKey(Property_char, verbose_name=u'Имя')
    value_property = models.CharField(max_length=200, verbose_name=u'Значение')

    class Meta:
        verbose_name = "Значение свойств"
        verbose_name_plural = "Значений свойств"

    def __str__(self):
        return str(self.name_property)


class Essential_prop(models.Model):
    relation_answer = models.ForeignKey(
        Answer, verbose_name=u'Вопрос')
    name_property = models.ForeignKey(Property_char)
    value_property = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Свойство вопросов"
        verbose_name_plural = "Свойства вопросов"

    def __str__(self):
        return str(self.id)


class User_rezult(models.Model):

    user_output = models.ForeignKey(User)
    question_output = models.CharField(max_length=200)    
    answer_output = models.ForeignKey(Answer,blank = True,null = True)
    type_quest = models.CharField(max_length=200)
    point = models.IntegerField(default=0)
    money = models.IntegerField(default=0)
    session_output = models.CharField(max_length=36)
    date_create = models.DateTimeField(auto_now=True)
    best_choise = models.CharField(max_length=150)

    def displaying(self):
        d = {}
        d["user_output"] = self.user_output

        d["question_output"] = self.question_output
        d["best_choise"] = self.best_choise

        d["answer_output"] = self.answer_output
        d["point"] = self.point
        d["money"] = self.money
        return d

    def __unicode__(self):
        return self.session_output

    def __str__(self):
        return self.session_output


class Tying_products(models.Model):
    name = models.CharField(max_length=150,verbose_name=u'Имя')
    price = models.IntegerField(default=0,verbose_name=u'Цена')

    class Meta:
        verbose_name = "Сопутствующий товар"
        verbose_name_plural = "Сопутствующие товары"

    def __str__(self):
        return self.name


class Relations_tying_products(models.Model):
    product = models.ForeignKey(Products,verbose_name=u'Товар')
    tying_product = models.ForeignKey(Tying_products,verbose_name=u'Сопутствующий товар')
    class Meta:
        verbose_name = "Сопутствующий товар для основного товара"
        verbose_name_plural = "Сопутствующие товары для основного товара"



