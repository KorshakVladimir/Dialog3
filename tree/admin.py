from django.contrib import admin

from . models import *


class QuestionsInline(admin.TabularInline):
    # list_display = ('text_answer','point_answer','questions_answer')
    model = Questions


class AnswerAdmin(admin.ModelAdmin):
    list_display = ( 'stage','id', 'text_answer')
    inlines = [
        QuestionsInline,
    ]


class User_rezultAdmin(admin.ModelAdmin):
    list_display = (
       'session_output', 'user_output', 'answer_output', 'date_create')


class QuestionsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'text_questions', 'relation_answer')


admin.site.register(Questions, QuestionsAdmin)

admin.site.register(Answer, AnswerAdmin)

admin.site.register(User_rezult, User_rezultAdmin)


@admin.register(Property_char)
class Property_charAdmin(admin.ModelAdmin):
    pass


class Relations_tying_products_Inline(admin.TabularInline):

    model = Relations_tying_products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    
    inlines = [
        Relations_tying_products_Inline,
    ]


@admin.register(Products_property)
class Products_propertyAdmin(admin.ModelAdmin):
    list_display = ('products','name_property', 'value_property')


@admin.register(Essential_prop)
class Essential_propAdmin(admin.ModelAdmin):
    pass


@admin.register(Tying_products)
class Tying_productsAdmin(admin.ModelAdmin):
    list_display= ["id","name"]
    pass


@admin.register(Stages)
class StagesAdmin(admin.ModelAdmin):
    list_display= ["id","name"]
    pass