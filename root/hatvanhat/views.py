from django import views
from django.shortcuts import render


# Create your views here.
class Home(views.View):

    def get(self, request):
        return render(request, 'index.html')


def start_game(game):
    game.number_of_players = len(game.players.all()) # TODO
