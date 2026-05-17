from django.db import models
from django.db.models import Sum

class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    stadium = models.CharField(max_length=100)
    logo_url = models.URLField(max_length=500, null=True, blank=True)
    founded_year = models.PositiveIntegerField(null=True, blank=True)

    @property
    def total_market_value(self):
        # Calculates the total value of all players in the team
        return self.players.aggregate(total=Sum('market_value'))['total'] or 0

    def __str__(self):
        return self.name

class Player(models.Model):
    POSITIONS = [('GK', 'Goalkeeper'), ('DF', 'Defender'), ('MF', 'Midfielder'), ('FW', 'Forward')]
    
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    position = models.CharField(max_length=2, choices=POSITIONS)
    jersey_number = models.PositiveIntegerField()
    market_value = models.DecimalField(max_digits=12, decimal_places=2)
    photo_url = models.URLField(max_length=500, null=True, blank=True)
    is_injured = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

class PlayerStats(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, related_name='stats')
    goals = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    yellow_cards = models.PositiveIntegerField(default=0)
    red_cards = models.PositiveIntegerField(default=0)
    minutes_played = models.PositiveIntegerField(default=0)