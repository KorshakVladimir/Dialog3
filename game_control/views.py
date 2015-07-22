from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import GameForm

def add_game(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GameForm()

    return render(request, 'game_control/add.html', {'form': form})

def del_game(request):
    pass