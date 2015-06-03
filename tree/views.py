
# -*- coding: utf-8 -*-

from django.shortcuts import render
from . models import *
import hashlib
import random


def res_product(request, id_prod, id_quest):
    prod = Products.objects.get(id=id_prod)
    guid = request.session.get('GUID')
    answers = [
        x.answer_output for x in User_rezult.objects.filter(session_output=guid)]
    proper_s = Essential_prop.objects.filter(relation_answer__in=answers)
    answer_exit = Answer.objects.get(id=48)
    quest_exit = Questions.objects.get(id=id_quest)
    # import pdb
    # pdb.set_trace()
    if proper_s:

        count_prop = 100 // len(proper_s)
        count_point = 0
        for i in proper_s:
            req_prop = Products_property.objects.filter(
                products=prod, name_property=i.name_property)
            if req_prop:
                if req_prop[0].value_property == i.value_property:
                    count_point += count_prop

        rezult = User_rezult(session_output=request.session.get('GUID'),
                             user_output=request.user,
                             point=count_point,
                             product=prod,
                             question_output=quest_exit,
                             answer_output=answer_exit
                             )
        rezult.save()
    return index(request, 48, id_quest)


def for_game(request, answer_id, id_quest, context):
    if int(answer_id) == 48:
        return context

    answer = Answer.objects.get(id=answer_id)
    questions = Questions.objects.filter(relation_answer_id=answer.id)

    question_output = ''
    product = Products.objects.all()

    list_product = []
    for el_product in product:

        prop = {}
        products_property = Products_property.objects.filter(
            products_id=el_product.id)
        dict_prod = {'name': el_product,
                     'description': el_product.description, 'property': products_property}

        list_product.append({"product": dict_prod})

    if answer_id == 1081:

        random_seq = str(random.random()).encode('utf-8')
        salt = hashlib.sha1(random_seq).hexdigest()[:36]
        request.session['GUID'] = salt
        request.session['point'] = 0
        request.session['emo'] = 50
    else:

        question_output = Questions.objects.get(
            id=id_quest)
        ansver_output = Answer.objects.get(
            id=question_output.relation_answer.id)
        quest_for_best_choise = Questions.objects.filter(
            relation_answer_id=ansver_output.id)
        best_choise = quest_for_best_choise[0]
        for i in quest_for_best_choise:
            if best_choise.point_answer < i.point_answer:
                best_choise = i

        rezult = User_rezult(session_output=request.session.get('GUID'),
                             user_output=request.user,
                             answer_output=ansver_output,
                             point=question_output.point_answer,
                             question_output=question_output,
                             best_choise=best_choise.id
                             )
        rezult.save()
    if question_output:
        point = question_output.point_answer
    else:
        point = 0

    context['point'] = request.session.get('point') + point
    context['emo'] = request.session.get('emo') + point
    context['answer'] = answer
    context['questions'] = questions
    context['list_product'] = list_product

    return context


def for_history(request, context):
    dict_sesions = {}
    list_sesions = []
    result = User_rezult.objects.filter(user_output=request.user)

    for i in result:
        dict_sesions[i.session_output] = i.date_create

    for key_d in dict_sesions:
        list_sesions.append(
            {'session_output': key_d, 'date_create': dict_sesions[key_d]})
    # import pdb
    # pdb.set_trace()
    context["list_sesions"] = list_sesions
    context['count'] = 0
    return context


def index(request, answer_id=1081, id_quest=0):

    context = {}
    context = for_game(request, answer_id, id_quest, context)
    context = for_history(request, context)
    context["active_game"] = 'active'
    context["active_jurnal"] = ''
    context["active_game_in"] = 'active in'
    context["active_jurnal_in"] = ''
    if int(answer_id) == 48:

        return game_history(request, request.session.get('GUID'))
    else:
        return render(request, 'gameplace.html', context)


# def history(request):

#     dict_sesions = {}
#     list_sesions = []
#     result = User_rezult.objects.filter(user_output=request.user)

#     for i in result:
#         dict_sesions[i.session_output] = i.date_create

#     for key_d in dict_sesions:
#         list_sesions.append(
#             {'session_output': key_d, 'date_create': dict_sesions[key_d]})
# import pdb
# pdb.set_trace()
#     context = {"list_sesions": list_sesions}
#     context['count'] = 0
#     return render(request, 'tree/history.html', context)
def for_game_history(request, guid, context):
    list_history = []

    history_entry = User_rezult.objects.filter(session_output=guid)
    order_history = history_entry.order_by('date_create')
    total_point = 0
    for i in order_history:
        if i.best_choise:
            best_choise = Questions.objects.get(id=int(i.best_choise))
        else:
            best_choise = ""
        # print(best_choise)
        total_point += i.point
        entry_order_history = i.displaying()
        # import pdb
        # pdb.set_trace()
        list_history.append({"answer_output": entry_order_history["answer_output"],
                             "question_output": entry_order_history["question_output"],
                             "best_choise": best_choise,
                             "point": entry_order_history["point"],
                             })
    context['history_entry'] = list_history
    context['total_point'] = total_point
    return context


def game_history(request, guid):
    context = {}
    context = for_game_history(request, guid, context)
    context = for_game(request, 1081, 0, context)
    context["active_game"] = ''
    context["active_jurnal"] = 'active'
    context["active_game_in"] = ''
    context["active_jurnal_in"] = 'active in'

    return render(request, 'tree/game_history_2.html', context)
