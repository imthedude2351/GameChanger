from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=150)
    developer = models.CharField(max_length=200)
    rating = models.CharField(max_length=5)
    year = models.IntegerField()

    def __str__(self):
        return self.name
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