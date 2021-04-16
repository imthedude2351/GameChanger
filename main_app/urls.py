from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/<int:game_id>/', views.games_detail, name='detail'),
    path('games/', views.games_index, name='index'),
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
    path('games/favorite/', views.favorite_index, name='favorite_index'),
    path('games/favorite/<int:game_id>/', views.favorite_create, name='favorite_create'),
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
    path('games/<int:game_id>/reviews/', views.reviews_create, name='reviews_create'),
    path('accounts/signup/', views.signup, name='signup'),
]
