from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game
from .forms import ReviewForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', { 'games': games })

def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    review_form = ReviewForm()
    return render(request, 'games/detail.html', { 'game': game, 'review_form': review_form })



class GameCreate(CreateView):
  model = Game
  fields = '__all__'


class GameUpdate(UpdateView):
  model = Game
  # Let's disallow the renaming of a Game by excluding the name field!
  fields = '__all__'

class GameDelete(DeleteView):
  model = Game
  success_url = '/games/'

def reviews_create(request, game_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.game_id = game_id
    new_review.save()
  return redirect('detail', game_id = game_id)
