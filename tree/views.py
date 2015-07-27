
# -*- coding: utf-8 -*-
from django.db.models import Sum
from django.shortcuts import render, HttpResponse
from . models import *
import hashlib
import random                                         
import pdb
from . forms  import AnswerForm
import re

from django.core.context_processors import csrf
from django.views.decorators.csrf import ensure_csrf_cookie
import pdb
import json
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required




def get_prod_all(context):
    product = Products.objects.all()
    list_product = []

    for el_product in product:

        prop = {}
        products_property = Products_property.objects.filter(
            products_id=el_product.id)
        dict_prod = {'name': el_product,
                     'description': el_product.description, 'property': products_property}

        list_product.append({"product": dict_prod})

    context['list_product'] = list_product
    return context

def get_stage(context):
    
    ob_stages = Stages.objects.all()
    context["stages"] = ob_stages
    return context

def tying_product(request,id_tying=0):
    return game_history(request, request.session.get('GUID'))
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

    if int(id_tying) == 1:
        return game_history(request, request.session.get('GUID'))
    else:
        return render(request,"tree/tying.html", context)

def part_prod(request):
    context = {}
    context = get_prod_all(context)
    return render(request,"tree/product.html", context)

def res_product(request, id_prod):
    
    # questions = Questions.objects.get(id =id_quest)
    # id_ans = int(questions.question_answer)
    # if id_ans==0:
    #    ob_ans = Answer.objects.get(id  = questions.relation_answer.id)
    #    id_ans =  ob_ans.id
    # answer = Answer.objects.get(id = id_ans)
    # prod = Products.objects.get(id=id_prod)
    # tyings = Relations_tying_products.objects.filter(product = prod)
    # list_id = [str(x.tying_product.id) for x in tyings]
    # s_tyings = ",".join(list_id)
    
    # request.session["s_tyings"] = s_tyings
    
    # guid = request.session.get('GUID')
    # answers = [
    #     x.answer_output for x in User_rezult.objects.filter(session_output=guid)]
    # proper_s = Essential_prop.objects.filter(relation_answer__in=answers)

  
    # count_point =0
    # if proper_s:

    #     count_prop = 100 // len(proper_s)
    #     count_point = 0
    #     for i in proper_s:
    #         req_prop = Products_property.objects.filter(
    #             products=prod, name_property=i.name_property)
    #         if req_prop:
    #             if req_prop[0].value_property == i.value_property:
    #                 count_point += count_prop
    # try:
    #     rezult = User_rezult(session_output=request.session.get('GUID'),
    #                              user_output=request.user,
    #                              point=count_point,
    #                              question_output=prod.name,
    #                              money = prod.price,
    #                              answer_output = answer,
    #                              )
    #     rezult.save()
    # except:
    #     pass
        
    return tying_product(request)


def for_game(request, answer_id, id_quest, context):

    question_output = ''
        
    context = get_prod_all(context)
    
    MIN_ANS = request.session.get('MIN_ANS')
    if MIN_ANS == answer_id :
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

    if int(answer_id) == 0:
        return context
    try:
        answer = Answer.objects.get(id=answer_id)
        questions = Questions.objects.filter(relation_answer_id=answer.id)
    except :
        answer = ''
        questions = ''
        pass    
 
    if question_output:
        point = question_output.point_answer
    else:
        point = 0
    current_point = request.session.get('point') + point
    current_emo = request.session.get('emo') + point

    request.session['point'] = current_point
    request.session['emo'] = current_emo
      
    context['point'] = current_point
    context['emo'] = current_emo
    context['answer'] = answer
    context['questions'] = questions
 

    return context


def for_history(request, context,game_id):
    dict_sesions = {}
    list_sesions = []

    query_text = r'''SELECT 
        session_output AS session_output,
        max(date_create) AS date_create,
        sum(point) AS point,
        sum(money) AS money
     
        FROM   tree_user_rezult AS rez
        LEFT JOIN  tree_answer AS  ans ON rez.answer_output_id = ans.id
        GROUP by session_output
        ORDER by  max(date_create)
        WHERE user_output_id = %s AND game_id = %s '''

    for rez in User_rezult.objects.raw(query_text, [request.user.id,game_id]):
        list_sesions.append(
            {'session_output': rez.session_output, 'date_create': rez.date_create, "point":rez.point,
            'money':rez.money})


    context["list_sesions"] = list_sesions
    context['count'] = 0
    return context

def select_prof(request):

    context= {}
    return render(request, 'tree/select_type_person.html', context)


    
@login_required(login_url='/login/')
def index(request, answer_id=-1, id_quest=0):
    
    context = {}
    game_id = request.session.get("game_id")
    try:
        context["answer"] = -1
        if answer_id == -1:
            answer_id  = MIN_ANS= Answer.objects.filter(game_id = game_id).order_by("id")[0].id
            request.session["MIN_ANS"] = MIN_ANS
        context = for_game(request, answer_id, id_quest, context)

    except:
        pass

    if not context["answer"]:
        return game_history(request, request.session.get('GUID'))
    else:
        return render(request, 'gameplace.html', context)

@login_required(login_url='/login/')
def profile(request):

    context = {}
   
    return render(request, 'tree/myprofile.html', context)
@login_required(login_url='/login/')
def history(request):
    context = {}
    game_id = request.session.get("game_id")
    context = for_history(request, context,game_id)
    
    return render(request, 'tree/history_1.html', context)
@login_required(login_url='/login/')
def statistic(request):
    context = {}
    
    return render(request, 'tree/statistic.html', context)

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

@login_required(login_url='/login/')
def game_history(request, guid):
    context = {}
    context = for_game_history(request, guid, context)
    
    return render(request, 'tree/game_history_2.html', context)


def refer(request):

    return render(request, 'tree/refer.html')
@login_required(login_url='/login/')
def diagram(request):
    game_id = request.session.get("game_id")
    list_all_answer = []
    try:
        firsk_ask = Answer.objects.filter(game_id =game_id ).order_by("id")[0]
        list_all_answer.append(firsk_ask)
    except :
        pass
    
    context = {}
    list_answer = []
    top = 200
    left = 5
    flag_answer = []
    list_con = []
    form = ""
    context = get_stage(context)
    while True:

        list_quest_answer = []
        step_top = 230
        top -= int(len(list_all_answer)*step_top/2)
        
        for el_answer in list_all_answer:

            all_quest = Questions.objects.filter(relation_answer_id = el_answer.id)
            
            list_answer.append({"el_answer":el_answer,"all_quest":all_quest,"top":top,"left":left})
            flag_answer.append(el_answer.id)
            for el_quest in all_quest: 
                if el_quest.question_answer:

                    list_con.append({"source":el_quest.id,"target":el_quest.question_answer})
                    try:
                        answer_instance = Answer.objects.get(id = int(el_quest.question_answer))

                        if not answer_instance.id in flag_answer:

                            flag_answer.append(answer_instance.id)
                            list_quest_answer.append(answer_instance)
                    except :
                        pass    
            top += step_top       
        left += 200
        
        list_all_answer = list_quest_answer

        if not list_quest_answer:
            break 
          
    context['list_answer']  = list_answer  
    context['list_con']     = list_con  
    context['form']         = form  
    return render(request, 'tree/Uml/digrama.html',context)

def new_ask(request):

    
    id = request.session.get('id_ans')

    if not id:
        try:
            
            inst_answer = Answer.objects.all().order_by('-id')[0]
            id = inst_answer.id
        except:
            id = 0
    else:
        id = int(id) 

    id+=1

    request.session["id_ans"] = id

    el_ans = Answer(id)
    el_ans.save()
    
    
    context = {"el_list":{"el_answer":{"id":id}}}
    context = get_stage(context)
    return render(request, 'tree/Uml/el_ask.html',context)


def load_button(request):
    context = {}

    if request.POST:
        href = request.POST.get("href")
        
        p = re.compile(r'^/tree/(?P<answer_id>\d*)/(?P<id_quest>\d*)$')
        par = p.search(href)
        
        answer_id = int(par.group("answer_id"))
        id_quest = int(par.group("id_quest"))
   
        context = for_game(request, answer_id, id_quest, context)

        return render(request,'tree/load_button.html',context)

def new_quest(request):

    context = {}
    if request.POST:
        max_id = int(request.POST.get("max_id"))
        max_id+=1
        context["el_quest"] = {"id":max_id}
    return render(request, 'tree/Uml/el_question.html',context)

def diagrama_save(request):

    game_id = request.session.get("game_id")

    if request.POST:
        
        srt_json = request.POST.get("json_str")
        d = json.loads(srt_json)

        for id_ask in d:

            ob_ask, create = Answer.objects.get_or_create(id = id_ask)
            ob_ask.game_id = game_id
            ob_ask.text_answer = d[id_ask]["ask"]['text_answer']
            tetxt_satge = d[id_ask]["ask"]['stage']
            ob_stage =  Stages.objects.filter(name = tetxt_satge )
            if ob_stage:

                ob_ask.stage = ob_stage[0] 

            ob_ask.save()
        
            for id_quest in d[id_ask]["questions"]:
                
                ob_quest, create = Questions.objects.get_or_create(id = id_quest)
                ob_quest.relation_answer = ob_ask
                ob_quest.question_answer = "0"
                d_attr = d[id_ask]["questions"][id_quest]
                     
                for attr_quest in d_attr:
                    
                    setattr(ob_quest, attr_quest, d_attr[attr_quest])
                    
                ob_quest.save()             
         
    return HttpResponse("")

def for_edit_new_row(request):
    context = {}
    if request.POST:
        max_id = request.POST.get("max_id")
        context["el_quest"] = {"id":int(max_id)+1}

    return render(request, 'tree/Uml/row_all_table.html',context)
    