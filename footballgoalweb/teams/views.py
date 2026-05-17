from django.shortcuts import render, get_object_or_404, redirect
from .models import Team, Player
from .forms import PlayerForm

def player_create(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PlayerForm()
    return render(request, 'teams/player_form.html', {'form': form, 'title': 'Add New Player'})

def player_update(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    if request.method == "POST":
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_detail', player_id=player.id)
    else:
        form = PlayerForm(instance=player)
    return render(request, 'teams/player_form.html', {'form': form, 'title': 'Edit Player'})

def player_delete(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    if request.method == "POST":
        player.delete()
        return redirect('home')
    return render(request, 'teams/player_confirm_delete.html', {'player': player})
def home(request):
    teams = Team.objects.all()
    players = Player.objects.select_related('team', 'stats').all()
    
    query = request.GET.get('q')
    team_id = request.GET.get('team')

    if query:
        players = players.filter(full_name__icontains=query)
    
    if team_id:
        players = players.filter(team_id=team_id)

    context = {
        'teams': teams,
        'players': players,
        'current_team': int(team_id) if team_id else None,
        'query': query,
    }
    return render(request, 'teams/home.html', context)

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    players = team.players.all()
    return render(request, 'teams/team_detail.html', {'team': team, 'players': players})

def player_detail(request, player_id):
    player = get_object_or_404(Player.objects.select_related('team', 'stats'), id=player_id)
    return render(request, 'teams/player_detail.html', {'player': player})

def transfer_player(request, player_id):
    return redirect('home')