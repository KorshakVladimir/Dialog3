
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Answer(models.Model):
    text_answer = models.CharField(
        max_length=200, verbose_name=u'Текст ответа')

    depth = models.IntegerField(default=0)

    def __unicode__(self):
        return self.text_answer

    def __str__(self):
        return self.text_answer


class Questions(models.Model):
    point_answer = models.IntegerField(default=0, verbose_name=u'Очки ответа')
    point_emotions = models.IntegerField(
        default=0, verbose_name=u'Очки емоций')

    text_questions = models.CharField(
        max_length=200, verbose_name=u'Текст Вопроса')
    relation_answer = models.ForeignKey(
        Answer, verbose_name=u'Вопрос для связи')

    question_answer = models.CharField(
        verbose_name=u'Вопрос для перехода', max_length=200)

    def __unicode__(self):
        return self.text_questions

    def __str__(self):
        return self.text_questions


class Property_char(models.Model):
    name_property_char = models.CharField(max_length=200)
    name_property_trans = models.CharField(max_length=200)

    def __str__(self):
        return self.name_property_char


class Products(models.Model):
    name = models.CharField(max_length=200)
    type_prod = models.CharField(max_length=200)
    description = models.TextField()
    image_product = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Products_property(models.Model):
    products = models.ForeignKey(Products)
    name_property = models.ForeignKey(Property_char)
    value_property = models.CharField(max_length=200)

    def __str__(self):
        return self.name_property


class Essential_prop(models.Model):
    relation_answer = models.ForeignKey(
        Answer, verbose_name=u'Вопрос для связи')
    name_property = models.ForeignKey(Property_char)
    value_property = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)


class User_rezult(models.Model):
    user_output = models.ForeignKey(User)
    question_output = models.ForeignKey(Questions)
    answer_output = models.ForeignKey(Answer)
    point = models.IntegerField(default=0)
    session_output = models.CharField(max_length=36)
    date_create = models.DateTimeField(auto_now=True)
    best_choise = models.CharField(max_length=150)
    product = models.ForeignKey(Products, blank=True, null=True)

    def displaying(self):
        d = {}
        d["user_output"] = self.user_output
        if self.product:
            d["question_output"] = self.product
            d["best_choise"] = ""
        else:
            d["question_output"] = self.question_output
            d["best_choise"] = self.best_choise

        d["answer_output"] = self.answer_output
        d["point"] = self.point
        return d

    def __unicode__(self):
        return self.session_output

    def __str__(self):
        return self.session_output
