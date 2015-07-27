from django.conf.urls import include, url
from . views import *


urlpatterns = [

    url(r'^add_game/$', add_game, name='add_game'),
    url(r'^edit_game/$', edit_game, name='edit_game'),
    url(r'^del_game/$', del_game, name='edit_game'),
    url(r'^gameplace/$', gameplace, name='gameplace'),
    url(r'^(?P<game_id>\d*)/$', run_game, name='run_game'),
]
