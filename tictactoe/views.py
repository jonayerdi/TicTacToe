from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Game
from .forms import CreateUserForm

def main_page(request):
    users = User.objects.all().order_by('username')
    challenges = Game.objects.filter(user2=request.user.pk).filter(outcome=-2).order_by('created_date')
    user_games = Game.objects.filter(Q(user1=request.user.pk) | Q(user2=request.user.pk)).filter(Q(outcome=-2) | Q(outcome=-1)).order_by('created_date')
    games = Game.objects.filter(Q(outcome=-2) | Q(outcome=-1)).order_by('created_date')[:64]
    return render(request, 'tictactoe/main_page.html', {'users': users, 'challenges': challenges, 'user_games': user_games, 'games': games})

def game_page(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if game.outcome==-2:
        game.outcome=-1
        game.save()
    return render(request, 'tictactoe/game_page.html', {'game': game})
    
def create_user(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            usr = form.save(commit=False)
            user = User.objects.create_user(username=usr.username, password=usr.password)
            return redirect('login')
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            userName = request.username
            userPass = request.password
            user = User.objects.create_user(username=userName, password=userPass)
            return redirect('login')
    else:
	    form = CreateUserForm()
    return render(request, 'registration/create_user.html', {'form': form})

    