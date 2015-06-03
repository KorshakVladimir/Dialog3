from django.contrib import admin

from . models import *


class QuestionsInline(admin.TabularInline):
    # list_display = ('text_answer','point_answer','questions_answer')
    model = Questions


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_answer')
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


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(Products_property)
class Products_propertyAdmin(admin.ModelAdmin):
    pass


@admin.register(Essential_prop)
class Essential_propAdmin(admin.ModelAdmin):
    pass
