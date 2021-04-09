from django.shortcuts import render
from django.http import HttpResponse

class Game: 
    def __init__(self, name, developer, rating, year):
        self.name = name
        self.developer = developer
        self.rating = rating
        self.year = year

games = [
    Game('The Last of Us 2', 'Naughty Dog', 'M', 2020),
    Game('Call of Duty: Black Ops', 'TreyArch', 'M', 2010),
    Game('StarCraft 2', 'Blizzard', 'T', 2010),
    Game('Ghost of Tsushima', 'Sucker Punch Production', 'M', 2020)
]


# Create your views here.
def home(request):
  return HttpResponse('<h1>Welcome to Game Changer</h1>')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    return render(request, 'games/index.html', { 'games': games })
