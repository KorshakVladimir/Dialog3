from django.shortcuts import render
from django.http import HttpResponse
from . forms import GameForm
from . models import Game

from tree.views import index

def add_game(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponse('done')
    else:
        form = GameForm()

    return render(request, 'game_control/add.html', {'form': form})

def edit_game(request):
    context = {}
    games = Game.objects.all()
    context["games"] = games

    return render(request, 'game_control/edit_games.html', context)

def del_game(request):
    if request.method == 'POST':
        game_id = request.POST.get("game_id")
        done = False
        try:
            game =  Game.objects.get(id = int(game_id)) 
            game.delete()
            done = True
        except :
            pass

    return HttpResponse(done)

def all_games(context): 
    context["games"] = Game.objects.all()
    return context

def all_game_menu(request):
    
    context = {}
    context = all_games(context)

    return render(request, "game_control/for_ajax/all_game.html",context)

def gameplace(request):
    context = {}
    context = all_games(context)
    return render(request, "stub.html",context)

def run_game(request, game_id ):
    request.session["game_id"] = game_id
    return index(request)

def config_game(request, game_id = 0 ):
    
    el_Game  = Game.objects.get(id = game_id)

    if request.method == 'POST':
        form = GameForm(request.POST, instance = el_Game)

        if form.is_valid():
            form.save()
            return HttpResponse('done')
    else:
        
        form = GameForm(instance=el_Game)
        
    return render(request, 'game_control/game_config.html', {'form': form,"game_id":game_id})
