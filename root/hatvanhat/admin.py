from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_profile', 'created', 'last_used')


@admin.register(models.Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'players_display', 'number_of_players', 'does_ended', 'pakli')

    def players_display(self, obj):
        return ',  '.join(map(str, obj.players.all()))

