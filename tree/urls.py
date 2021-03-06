from django.conf.urls import include, url
from . views import *


urlpatterns = [
    url(r'^session/(?P<guid>.*)/$', game_history, name='game_history'),
    url(r'^$', refer, name='refer'),
    url(r'^new_ask/$', new_ask, name='new_ask'),
    url(r'^new_quest/$', new_quest, name='new_quest'),
    url(r'^part_prod/$', part_prod, name='part_prod'),
    url(r'^for_edit_new_row/$', for_edit_new_row, name='for_edit_new_row'),
    url(r'^select_prof/$', select_prof, name='select_prof'),
    url(r'^history/$', history, name='history'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^statistic/$', statistic, name='statistic'),
    url(r'^index/$', index, name='index_empty'),
    url(r'^(?P<answer_id>\d*)/(?P<id_quest>\d*)$', index, name='index'),
    url(r'^prod/(?P<id_prod>\d*)', res_product, name='res_product'),
    url(r'^tying/(?P<id_tying>\d*)$', tying_product, name='tying_product'),
    url(r'^diagrama/$', diagram, name='diagram'),
    url(r'^diagrama_save/$', diagrama_save, name='diagrama_save'),
    url(r'^load_button/$', load_button, name='load_button'),
]
