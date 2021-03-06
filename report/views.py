from django.shortcuts import render
import json
from django.http import HttpResponse
from tree.models import  *
import pdb

from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def radar_chart_game(request):

    js_dat = {}
    
    obstages = Stages.objects.all()
    
    for stage in obstages:
        js_dat[stage.id] = {"stage_name":stage.name}
        js_dat[stage.id]["total_point"] = 0
        js_dat[stage.id]["max_total_point"] = 0
        ob_ans_s = Answer.objects.filter(stage = stage)
        sum_point_ans = 0

        for ans in ob_ans_s:

            ob_quest_s = Questions.objects.filter(relation_answer = ans)

            maxpoint_quest = 0
            for question in ob_quest_s:
                if maxpoint_quest < question.point_answer:
                    maxpoint_quest = question.point_answer
            sum_point_ans+= maxpoint_quest

        js_dat[stage.id]["max_point"] = sum_point_ans   


    history_entrys_sesions = User_rezult.objects.values("session_output")
    
    
    
    ses_dict = {}
    for ses in history_entrys_sesions:
        ses_id =  ses["session_output"]
        entr_answer = User_rezult.objects.filter(session_output = ses_id)
        stage_dict = {}
        for entry in entr_answer:
            if entry.answer_output:
                if entry.answer_output.stage:

                    if not entry.answer_output.stage in stage_dict:
                                stage_dict[entry.answer_output.stage] = 0

                    stage_dict[entry.answer_output.stage] += entry.point

        ses_dict[ses_id] = stage_dict    

    
    for key_ses in ses_dict:

        el_stage = ses_dict[key_ses]

        for stafe_key in el_stage:

            if stafe_key.id in js_dat:

                js_dat[stafe_key.id]["total_point"] += el_stage[stafe_key]
                js_dat[stafe_key.id]["max_total_point"] += js_dat[stafe_key.id]["max_point"]


    # pdb.set_trace()       

    #---------------------

    data = {}
    data['label']= []
    data['max_point'] = []
    data["user_point"] = []
    for key_dat in js_dat:

        data['label'].append(js_dat[key_dat]["stage_name"])
        # data['max_point'].append(int(js_dat[key_dat]["total_point"]/js_dat[key_dat]["max_total_point"]*100))
        data['max_point'].append(js_dat[key_dat]["max_total_point"])
        data['user_point'].append(js_dat[key_dat]["total_point"])
    print(data)    
    return HttpResponse(json.dumps(data), content_type = "application/json")