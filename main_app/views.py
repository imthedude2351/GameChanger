from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Game, Favorite, Review
from .forms import ReviewForm
import requests
from django.urls import  reverse_lazy, reverse
from django import http

@login_required
def home(request):
  games = Game.objects.all()
  return render(request, 'games/index.html', { 'games': games })

def about(request):
  return render(request, 'about.html')

@login_required
def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', { 'games': games })

@login_required
def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  review_form = ReviewForm()
  return render(request, 'games/detail.html', { 'game': game, 'review_form': review_form })


def search(request):
  search_term = request.POST.get('search_input')
  url = f"https://api.rawg.io/api/games?key=87dba13a6af3467581a4dc49007ba4d4&search={search_term}"
  r = requests.get(url).json()
  return render(request, 'games/api.html', {'data' : r['results'] })


def search_view(request):
  return render(request, 'games/search.html')



class GameCreate(LoginRequiredMixin, CreateView):
  model = Game
  fields = ['name', 'developer', 'rated', 'year']

  def form_valid(self, form):
  # Assign the logged in user (self.request.user)
    print(form)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)


class GameUpdate(LoginRequiredMixin, UpdateView):
  model = Game
  # Let's disallow the renaming of a Game by excluding the name field!
  fields = '__all__'

class GameDelete(LoginRequiredMixin, DeleteView):
  model = Game
  success_url = '/games/'

  # override the delete function to check for a user match
  def delete(self, request, *args, **kwargs):
      user = request.user
      # the Post object
      self.object = self.get_object()
      if self.object.user == request.user:
          success_url = self.get_success_url()
          self.object.delete()
          return http.HttpResponseRedirect(success_url)
      else:
          return http.HttpResponseForbidden("Cannot delete other's posts")

@login_required
def reviews_create(request, game_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.game_id = game_id
    new_review.save()
  return redirect('detail', game_id = game_id)

@login_required
def favorite_index(request):
    favs = request.user.favorite_set.all()
    return render(request, 'games/favorite.html', { 'favs' : favs }) 

@login_required
def favorite_create(request, game_id):
    favs = request.user.favorite_set.all()
    for fav in favs:
        if (game_id == fav.__dict__['game_id']):
            fav.delete()
            return redirect('favorite_index')
    else:
        instance = Favorite()
        instance.game_id = game_id
        instance.user = request.user
        instance.save()
        return redirect('detail', game_id = game_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class RevDelete(LoginRequiredMixin, DeleteView):
  model = Review
  def get_success_url(self):
    return reverse('detail', kwargs={'game_id': self.object.game.id})