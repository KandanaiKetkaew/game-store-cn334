from datetime import datetime
from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Game



def games(request):
    all_games = Game.objects.all()
    context = {'games': all_games}
    return render(request,'app_gamelist/games.html',context)

def game(request, game_id):
    one_game = None
    try:
        one_game = Game.objects.get(id=game_id)
    except:
        print('This game is not found')
    context = {'game': one_game}
    return render(request,'app_gamelist/game.html',context)