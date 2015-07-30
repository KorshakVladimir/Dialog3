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
from tree.models import *

def my_parse():
    query_text = r'''SELECT 
        session_output AS session_output,
        MAX(date_create) AS date_create,
        SUM(point) AS point,
        SUM(money) AS money
     
        FROM   tree_user_rezult AS rez
        LEFT JOIN  tree_answer AS  ans ON rez.answer_output_id = ans.id
        GROUP by session_output
        ORDER by  MAX(date_create)
        WHERE rez.user_output_id = %s AND ans.game_id = %s '''
    # for rez in User_rezult.objects.raw(te, [request.user.id, int(game_id)]):

    te = r''' SELECT * FROM tree_user_rezult '''

    query_text = r'''SELECT rez.id as id,
                    session_output AS session_output,
                    MAX(date_create) AS date_create,
                    SUM(point) AS point,
                    SUM(money) AS money
                    FROM   tree_user_rezult AS rez

                    LEFT JOIN  tree_answer AS  ans ON rez.answer_output_id = ans.id

                    WHERE rez.user_output_id = %s AND ans.game_id = %s 

                    GROUP by session_output

                    ORDER by  MAX(date_create)'''
    for rez in User_rezult.objects.raw(query_text,[1,33]):
        print(rez)
    return True

if __name__ == "__main__":
    print(my_parse())
