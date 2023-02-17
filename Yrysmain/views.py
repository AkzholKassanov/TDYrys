from django.shortcuts import render
from .models import Player

# Create your views here.
def MainPage(request):
    players = Player.objects.all().order_by('-score')
    for i, player in enumerate(players):
        player.id = i + 1  # add an 'id' attribute to each player object
    context = {'players': players}
    return render(request, 'index.html', context)

