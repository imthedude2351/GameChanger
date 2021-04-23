from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

RATINGS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=150)
    developer = models.CharField(max_length=200)
    rated = models.CharField(max_length=10)
    year = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # img_url = models.CharField(max_length=300)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})


class Review(models.Model):
    review = models.TextField(
        max_length=500)
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

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return f"{self.game_id}"