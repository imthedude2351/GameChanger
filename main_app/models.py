from django.db import models
from django.urls import reverse

RATINGS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

# Create your models here.
class Game(models.Model):
    name        = models.CharField(max_length=150)
    developer   = models.CharField(max_length=200)
    rated      = models.CharField(max_length=5)
    year        = models.IntegerField()

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})


class Review(models.Model):
    review = models.TextField(max_length=500)
    rating = models.CharField(
        max_length=1,
        choices=RATINGS,
        default=RATINGS[-1][-1]
    )

    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review} {self.rating}"

    class Meta:
        ordering = ['-id']




# class Game: 
#     def __init__(self, name, developer, rating, year):
#         self.name = name
#         self.developer = developer
#         self.rating = rating
#         self.year = year

# games = [
#     Game('The Last of Us 2', 'Naughty Dog', 'M', 2020),
#     Game('Call of Duty: Black Ops', 'TreyArch', 'M', 2010),
#     Game('StarCraft 2', 'Blizzard', 'T', 2010),
#     Game('Ghost of Tsushima', 'Sucker Punch Production', 'M', 2020)
# ]