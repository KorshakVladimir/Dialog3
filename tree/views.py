
# -*- coding: utf-8 -*-

from django.shortcuts import render
from . models import *
import hashlib
import random

def make_game(context):
    context["active_game"] = 'active'
    context["active_jurnal"] = ''
    context["active_game_in"] = 'active in'
    context["active_jurnal_in"] = ''
    return context


def tying_product(request,id_tying=0):
    context = {}
    context['point'] = request.session.get('point')
    context['emo'] = request.session.get('emo')
    inst_answer = Answer.objects.get(id = 47)
    context["answer"] = inst_answer
    id_tying = int(id_tying)
    s_tyings = request.session.get('s_tyings')
    list_tying = []
    if s_tyings:

        list_tying = list(map(lambda x :int(x),s_tyings.split(",")))
    # import pdb
    # pdb.set_trace()

    if id_tying in list_tying:
        
        list_tying.remove(id_tying)
        s_tyings = ",".join(map(lambda x :str(x),list_tying))
        request.session["s_tyings"] = s_tyings

    tying_instans = Tying_products.objects.filter(id__in = list_tying)

    if not id_tying == 0 and not id_tying == 1 :
        tying = Tying_products.objects.get(id  = id_tying)
        rezult = User_rezult(session_output=request.session.get('GUID'),
                 user_output=request.user,
                 question_output = tying.name,
                 money = tying.price,
                 answer_output = inst_answer
                 )
        rezult.save()

    context["tying_instans"] = tying_instans
    context = for_history(request, context)
    bay_quest = Tying_products.objects.get(id = 1)
    context["bay_quest"] = bay_quest
    context = make_game(context)

    
    
    if int(id_tying) == 1:
        return game_history(request, request.session.get('GUID'))
    else:
        return render(request,"tree/tying.html", context)


def res_product(request, id_prod, id_quest):
    
    questions = Questions.objects.get(id =id_quest)
    answer = Answer.objects.get(id = int(questions.question_answer))
    prod = Products.objects.get(id=id_prod)
    tyings = Relations_tying_products.objects.filter(product = prod)
    list_id = [str(x.tying_product.id) for x in tyings]
    s_tyings = ",".join(list_id)
    
    request.session["s_tyings"] = s_tyings
    
    guid = request.session.get('GUID')
    answers = [
        x.answer_output for x in User_rezult.objects.filter(session_output=guid)]
    proper_s = Essential_prop.objects.filter(relation_answer__in=answers)

    # import pdb
    # pdb.set_trace()
    count_point =0
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
                             question_output=prod.name,
                             money = prod.price,
                             answer_output = answer,
                             )
    rezult.save()
    return tying_product(request)


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
                             question_output=question_output.text_questions,
                             best_choise=best_choise.text_questions
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
    context = make_game(context)
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
    total_money = 0
    for i in order_history:

        best_choise = i.best_choise

        # print(best_choise)
        total_point += i.point
        total_money += i.money
        entry_order_history = i.displaying()
        # import pdb
        # pdb.set_trace()
        list_history.append({"answer_output": entry_order_history["answer_output"],
                             "question_output": entry_order_history["question_output"],
                             "best_choise": best_choise,
                             "point": entry_order_history["point"],
                             "money": entry_order_history["money"],
                             })
    context['history_entry'] = list_history
    context['total_point'] = total_point
    context['total_money'] = total_money
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
