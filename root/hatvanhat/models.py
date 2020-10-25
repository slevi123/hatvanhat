from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=14) #TODO: check if name is taken in the current game
    user_profile = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField(auto_now=True) #TODO: upgrade this value

    def __str__(self):
        if self.user_profile:
            return f"{self.user_profile}@{self.name}"
        else:
            return f"@{self.name}"


class Game(models.Model):
    player_numbers_choices = [
        (2, 'Ketto'),
        (3, 'Harom'),
        (4, 'Negy'),
        (1, '_Fuggoben_'),

    ]

    pakli = models.CharField(max_length=40, unique=False, blank=True)
    players = models.ManyToManyField(Player)
    start_date = models.DateTimeField(auto_now_add=True)
    does_ended = models.BooleanField(default=False)
    number_of_players = models.SmallIntegerField(choices=player_numbers_choices)
    # TODO: settings to be implemented (4: betli, kismars, nagymars pontszam)

    def __str__(self):
        return f"Game#{self.id} (p{self.number_of_players})"

