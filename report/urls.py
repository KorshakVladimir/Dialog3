from django.conf.urls import include, url
from . views import *


urlpatterns = [
    url(r'^radar_chart_game/$', radar_chart_game, name='radar_chart_game'),
]