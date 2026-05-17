from django.contrib import admin
from .models import Team, Player, PlayerStats

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(PlayerStats)