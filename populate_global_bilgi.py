# -*- coding: utf-8 -*-
import xml.etree.ElementTree as etree
import os
import django
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'cgm.settings')

django.setup()
from tree import models

from django.core.files import File
import urllib.request
from django.conf import settings


# def save_img(entry, path, img_filename):

#     response = urllib.request.urlopen(path)
#     with open('tmp_img', 'wb') as f:
#         f.write(response.read())

#     with open('tmp_img', 'rb') as f:
#         img_file = File(f)
#         entry.image_product.save(img_filename, img_file, True)
#     os.remove('tmp_img')


# def parse_id(id):
#     return int(str(ord(id[0])) + id[1:])


# def del_l(t):
#     return t.replace('~', ' ')


def my_parse():

    models.User_rezult.objects.all().delete()
    models.Answer.objects.all().delete()
    models.Questions.objects.all().delete()
    models.Property_char.objects.all().delete()
    models.Products.objects.all().delete()
    models.Products_property.objects.all().delete()
    models.Tying_products.objects.all().delete()
    models.Relations_tying_products.objects.all().delete()

   
    d = {
    "opml": {
        "head": {
            "title": "ГлобалБилги сценарий",
            "expansionState": "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16"
        },
        "body": {
            "outline": [
                {
                    "outline": {
                        "outline": [
                            {
                                "outline": {
                                    "outline": [
                                        {
                                            "outline": {
                                                "outline": [
                                                    {
                                                        "outline": {
                                                            "outline": {
                                                                "outline": [
                                                                    {
                                                                        "outline": {
                                                                            "outline": [
                                                                                {
                                                                                    "outline": {
                                                                                        "outline": [
                                                                                            {
                                                                                                "outline": {
                                                                                                    "outline": [
                                                                                                        {
                                                                                                            "outline": {
                                                                                                                "outline": {
                                                                                                                    "_text": "ПРЕДЛОЖЕНИЕ"
                                                                                                                },
                                                                                                                "_text": "СМС и звонки на все номера.",
                                                                                                                "_Стадия": "Прояснение запроса",
                                                                                                                "_Персонаж": "2",
                                                                                                                "_Optimal": "1",
                                                                                                                "_Баллы": "10"
                                                                                                            },
                                                                                                            "_text": "Планируете отправлять смс/звонить на номера life:) или на номера других операторов?",
                                                                                                            "_Стадия": "Прояснение запроса",
                                                                                                            "_Персонаж": "1",
                                                                                                            "_Optimal": "1",
                                                                                                            "_Баллы": "10"
                                                                                                        },
                                                                                                        {
                                                                                                            "_text": "Ирина, Вы планируете говорить только с абонентами Life?",
                                                                                                            "_Стадия": "Прояснение запроса",
                                                                                                            "_Персонаж": "1",
                                                                                                            "_Optimal": "0",
                                                                                                            "_Баллы": "5"
                                                                                                        },
                                                                                                        {
                                                                                                            "_text": "Планируете ли Вы звонить другим операторам, например Киевстар или МТС?",
                                                                                                            "_Стадия": "Прояснение запроса",
                                                                                                            "_Персонаж": "1",
                                                                                                            "_Optimal": "0",
                                                                                                            "_Баллы": "5"
                                                                                                        }
                                                                                                    ],
                                                                                                    "_text": "Примерно 100 сообщений и много разговоров.",
                                                                                                    "_Стадия": "Прояснение запроса",
                                                                                                    "_Персонаж": "2",
                                                                                                    "_Optimal": "1",
                                                                                                    "_Баллы": "10"
                                                                                                },
                                                                                                "_text": "Какой объем минутт разговоров и количество отправленных СМС Вас интересует?",
                                                                                                "_Стадия": "Прояснение запроса",
                                                                                                "_Персонаж": "1",
                                                                                                "_Optimal": "1",
                                                                                                "_Баллы": "10"
                                                                                            },
                                                                                            {
                                                                                                "_text": "Ирина, Вы, обычно, много отправляете смс и говорите?",
                                                                                                "_Стадия": "Прояснение запроса",
                                                                                                "_Персонаж": "1",
                                                                                                "_Optimal": "0",
                                                                                                "_Баллы": "5"
                                                                                            },
                                                                                            {
                                                                                                "_text": "Ирина, скажите, пожалуйста, Сколько минут смс вам нужно в месяц?",
                                                                                                "_Стадия": "Прояснение запроса",
                                                                                                "_Персонаж": "1",
                                                                                                "_Optimal": "0",
                                                                                                "_Баллы": "5"
                                                                                            }
                                                                                        ],
                                                                                        "_text": "В Киевской области",
                                                                                        "_Стадия": "Прояснение запроса",
                                                                                        "_Персонаж": "2",
                                                                                        "_Optimal": "1",
                                                                                        "_Баллы": "10"
                                                                                    },
                                                                                    "_text": "В какой области Украины будете пользоваться номером?",
                                                                                    "_Стадия": "Прояснение запроса",
                                                                                    "_Персонаж": "1",
                                                                                    "_Optimal": "1",
                                                                                    "_Баллы": "10"
                                                                                },
                                                                                {
                                                                                    "_text": "Могли бы Вы сказать, где вы проживаете?",
                                                                                    "_Стадия": "Прояснение запроса",
                                                                                    "_Персонаж": "1",
                                                                                    "_Optimal": "0",
                                                                                    "_Баллы": "5"
                                                                                },
                                                                                {
                                                                                    "_text": "Могли бы Вы сказать, В каком регионе Украины вы живете?",
                                                                                    "_Стадия": "Прояснение запроса",
                                                                                    "_Персонаж": "1",
                                                                                    "_Optimal": "0",
                                                                                    "_Баллы": "5"
                                                                                }
                                                                            ],
                                                                            "_text": "Хочу отправлять смс и совершать звонки.",
                                                                            "_Стадия": "После удержания",
                                                                            "_Персонаж": "2",
                                                                            "_Optimal": "1",
                                                                            "_Баллы": "10"
                                                                        },
                                                                        "_text": "Спасибо за то, что оставались на линии. У вас тарифный план LLL. Какими услугами планируете пользоваться?",
                                                                        "_Стадия": "После удержания",
                                                                        "_Персонаж": "1",
                                                                        "_Optimal": "1",
                                                                        "_Баллы": "10"
                                                                    },
                                                                    {
                                                                        "_text": "Что будете использовать?",
                                                                        "_Стадия": "После удержания",
                                                                        "_Персонаж": "1",
                                                                        "_Optimal": "0",
                                                                        "_Баллы": "5"
                                                                    }
                                                                ],
                                                                "_text": "Спасибо",
                                                                "_Стадия": "Удержание",
                                                                "_Персонаж": "1",
                                                                "_Optimal": "1",
                                                                "_Баллы": "10"
                                                            },
                                                            "_text": "да, конечно",
                                                            "_Стадия": "Удержание",
                                                            "_Персонаж": "2",
                                                            "_Optimal": "1",
                                                            "_Баллы": "10"
                                                        },
                                                        "_text": "Будет ли Вам удобно подождать на линии пока я проверю информацию для Вас?",
                                                        "_Стадия": "Удержание",
                                                        "_Персонаж": "1",
                                                        "_Optimal": "1",
                                                        "_Баллы": "10"
                                                    },
                                                    {
                                                        "_text": "Ирина, Какими услугами Вы планируете пользоваться?",
                                                        "_Стадия": "Удержание",
                                                        "_Персонаж": "1",
                                                        "_Optimal": "0",
                                                        "_Баллы": "5"
                                                    },
                                                    {
                                                        "_text": "Ирина, Какие услуги должны быть включены в тарифный план?",
                                                        "_Стадия": "Удержание",
                                                        "_Персонаж": "1",
                                                        "_Optimal": "0",
                                                        "_Баллы": "5"
                                                    }
                                                ],
                                                "_text": "Да, по этому номеру.",
                                                "_Стадия": "Уточнение номера",
                                                "_Персонаж": "2",
                                                "_Optimal": "1",
                                                "_Баллы": "10"
                                            },
                                            "_text": "Ирина, Вас интересует информация по номеру, с которого обращаетесь?",
                                            "_Стадия": "Запрос имени",
                                            "_Персонаж": "1",
                                            "_Optimal": "1",
                                            "_Баллы": "10"
                                        },
                                        {
                                            "_text": "Скажите, пожалуйста, номер телефона по которому нужно изменить тарифный план?",
                                            "_Стадия": "Запрос имени",
                                            "_Персонаж": "1",
                                            "_Optimal": "0",
                                            "_Баллы": "5"
                                        }
                                    ],
                                    "_text": "Ирина",
                                    "_Стадия": "Запрос имени",
                                    "_Персонаж": "2",
                                    "_Optimal": "1",
                                    "_Баллы": "10"
                                },
                                "_text": "Как я могу к Вам обращаться?",
                                "_Стадия": "Запрос имени",
                                "_Персонаж": "1",
                                "_Optimal": "1",
                                "_Баллы": "10"
                            },
                            {
                                "_text": "Скажите пожалуйста номер телефона по которому нужно изменить тарифный план?",
                                "_Стадия": "Запрос имени",
                                "_Персонаж": "1",
                                "_Optimal": "0",
                                "_Баллы": "5"
                            },
                            {
                                "_text": "Вас интересует информация по номеру, с которого обращаетесь?",
                                "_Стадия": "Запрос имени",
                                "_Персонаж": "1",
                                "_Optimal": "0",
                                "_Баллы": "5"
                            }
                        ],
                        "_text": "Здравствуйте. Я хотел бы изменить свой тарифный план.",
                        "_Стадия": "Приветствие ",
                        "_Персонаж": "2",
                        "_Optimal": "1",
                        "_Баллы": "10"
                    },
                    "_text": "Добрый день. Меня зовут Сергей. Чем я могу быть Вам полезен?",
                    "_Стадия": "Приветствие ",
                    "_Персонаж": "1",
                    "_Optimal": "1",
                    "_Баллы": "10"
                },
                {
                    "_text": "Добрый день, день чем могу Вам помочь?",
                    "_Стадия": "Приветствие ",
                    "_Персонаж": "1",
                    "_Optimal": "0",
                    "_Баллы": "5"
                },
                {
                    "_text": "Добрый день. Сергей, я Вас слушаю.",
                    "_Стадия": "Приветствие ",
                    "_Персонаж": "1",
                    "_Optimal": "0",
                    "_Баллы": "5"
                }
            ]
        },
        "_version": "1.0"
    }
    }


    id = 1081
    answer = models.Answer(id = id,text_answer = "Ало")
    answer.save()
    
    import pdb; 
    main_list = d['opml']['body']["outline"]
    while 1==1:
        id= id + 1
        # if id == 1090:
        #     id = 48
        print(id)
        sub_list = []   
        # pdb.set_trace()
        for i in main_list:
            # pdb.set_trace()
            try:                
                print(i["_text"])
            except :
                break
                pdb.set_trace()
            # if 'Планируете отправлять смс/звонить на номера life:) или на номера других операторов?' == i["_text"]:
            #     pdb.set_trace()
            
            models.Questions(text_questions = i["_text"],relation_answer = answer,question_answer = id,point_answer = int(i["_Баллы"]) ).save()
            

            if i["_Optimal"] == "1" :
                sub_list = i["outline"]
                if type(sub_list) is dict:
                    answer_next = models.Answer(id = id,text_answer = sub_list["_text"]) 
                    answer.save()
                    sub_list = sub_list["outline"]
                    if type(sub_list) is dict:
                        if not "_Optimal" in sub_list.keys():
                            continue
                        sub_list = [sub_list]
                        # pdb.set_trace()
                elif type(sub_list) is list:
                    pass
                else :
                    pass
                  
            # print(i["_text"])
        main_list = sub_list 
        answer = answer_next
        if not main_list:
            break;
        if id > 2000 :
            return False   

    answer = models.Answer(id = 1090,text_answer = "СМС и звонки на все номера.")
    answer.save()

    models.Questions(text_questions = "Предложение",relation_answer = answer,question_answer = 48 ,point_answer = 10 ).save()

    return True
    # --------------------------------------------------------------------------------
    # tree = etree.parse('Game_01.xml')

    # root = tree.getroot()
    # for level in root:  # levels

    #     Id = parse_id(level.find('Id').text)
    #     # import pdb; pdb.set_trace()
    #     for Questions in level.iter('Questions'):
    #         for Question in Questions.iter('Question'):

    #             text_answer = ''.join(
    #                 Question.find('Text').text)

    #             text_answer = del_l(text_answer)
    #             # print(str(Question.find('Text').text))
    #             answer_model = models.Answer(id=Id, text_answer=text_answer)
    #             answer_model.save()
    #             for Answers in Question.iter('Answers'):
    #                 for Answer in Answers.iter('Answer'):

    #                     id_question = int(
    #                         str(Id) + str(parse_id(Answer.find('Id').text)))

    #                     text_question = ''.join(
    #                         Answer.find('Text').text)
    #                     if str(id_question) == '1082397001' or str(id_question)[3:6] == '1081597001' \
    #                             or str(id_question)[3:6] == '1081497001' or str(id_question)[3:6] == '1081397001':
    #                         text_question = 'Предложить товар'

    #                     else:
    #                         text_question = del_l(text_question)
    #                     target = parse_id(Answer.find('Target').text)
    #                     point = int(Answer.find('Point').text)

    #                     question_model = models.Questions(id=id_question, point_answer=point,
    #                                                       text_questions=text_question, relation_answer=answer_model,
    #                                                       question_answer=target)
    #                     question_model.save()

    # ess_prop = models.Essential_prop(
    #     relation_answer_id=10810, name_property=internet, value_property='Да')
    # ess_prop.save()

    # model_zdrav = models.Answer.objects.get(id=1081)
    # test_quest = models.Questions(point_answer=50, point_emotions=-30,
    #                               text_questions="Предложить товар",
    #                               relation_answer=model_zdrav, question_answer=48)
    # test_quest.save()

    # el_quest = models.Questions.objects.get(id=1081397001)
    # el_quest.text_questions = "Предложить товар"
    # el_quest.save()

    # el_quest = models.Questions.objects.get(id=1081497001)
    # el_quest.text_questions = "Предложить товар"
    # el_quest.save()

    # el_quest = models.Questions.objects.get(id=1081597001)
    # el_quest.text_questions = "Предложить товар"
    # el_quest.save()

    # el_quest = models.Questions.objects.get(id=1082197001)
    # el_quest.text_questions = "Предложить товар"
    # el_quest.save()

    # mod_ans = models.Answer(id=48, text_answer="Выход")
    # mod_ans.save()
    # mod_ans = models.Answer(id=47, text_answer="Что вы мне хотите предложить?")
    # mod_ans.save()
    # mod_bay = models.Answer(id=47, text_answer="Попрощаться")
    # mod_bay.save()

    

    

if __name__ == "__main__":
    print(my_parse())
