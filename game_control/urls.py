from django.conf.urls import include, url
from . views import *


urlpatterns = [

    url(r'^add_game/$', add_game, name='add_game'),
    url(r'^del_game/$', del_game, name='del_game'),

]
