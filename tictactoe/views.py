from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Game
from .forms import CreateUserForm
from .game import GameLogic

def main_page(request):
    users = User.objects.all().order_by('username')
    challenges = Game.objects.filter(user2=request.user.pk).filter(outcome=-2).order_by('created_date')
    user_games = Game.objects.filter(Q(user1=request.user.pk) | Q(user2=request.user.pk)).filter(Q(outcome=-2) | Q(outcome=-1)).order_by('created_date')
    games = Game.objects.filter(Q(outcome=-2) | Q(outcome=-1)).order_by('created_date')[:64]
    return render(request, 'tictactoe/main_page.html', {'users': users, 'challenges': challenges, 'user_games': user_games, 'games': games})

def get_username(request, pk):
    user = get_object_or_404(User, pk=pk)
    return HttpResponse(user.username)
    
def get_challenge_list(request, pk):
    challenges = Game.objects.filter(user2=pk).filter(outcome=-2).order_by('created_date')
    challenges_serialized = serializers.serialize("json", challenges, fields=('user1','user2','user1_turn'))
    return HttpResponse(challenges_serialized)
    
def game_page(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.user==game.user2 and game.outcome==-2:
        game.outcome=-1
        game.save()
    return render(request, 'tictactoe/game_page.html', {'game': game})
    
def new_game(request, user2pk):
    if request.user.is_authenticated():
        user2 = User.objects.get(pk=int(user2pk))
        if request.user != user2:
            game = Game(user1=request.user, user2=user2)
            game.save()
            return redirect('/game/'+str(game.pk))
    return HttpResponse()
    
def get_board_state(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return HttpResponse(game.state)
    
def change_board_state(request, game_id, square):
    game = get_object_or_404(Game, pk=game_id)
    square = int(square)
    if (game.outcome==-2 or game.outcome==-1) and game.state[square]=='_':
        if request.user==game.user1 and game.user1_turn:
            game.state = game.state[:square] + 'X' + game.state[square + 1:]
            game.user1_turn = not game.user1_turn
            GameLogic.check_finish(game,square)
            game.save()
            return HttpResponse(game.state)
        elif request.user==game.user2 and not game.user1_turn:
            game.state = game.state[:square] + 'O' + game.state[square + 1:]
            game.user1_turn = not game.user1_turn
            GameLogic.check_finish(game,square)
            game.save()
            return HttpResponse(game.state)
    return HttpResponse(game.state)
    
def create_user(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            userName = request.POST['username']
            userPass = request.POST['password']
            user = User.objects.create_user(username=userName, password=userPass)
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'registration/create_user.html', {'form': form})

#REST API for third parties (Not used for page)

def get_user_list(request):
    users = User.objects.all()
    users_serialized = serializers.serialize("json", users, fields=('username','is_staff'))
    return HttpResponse(users_serialized)
    
def get_active_game_list(request):
    games = Game.objects.all().filter(Q(outcome=-2) | Q(outcome=-1)).order_by('created_date')
    games_serialized = serializers.serialize("json", games, fields=('user1','user2','user1_turn'))
    return HttpResponse(games_serialized)
	
def get_game_list_user(request, pk):
    games = Game.objects.all().filter(Q(user1=pk) | Q(user2=pk)).order_by('created_date').order_by('created_date')
    games_serialized = serializers.serialize("json", games, fields=('user1','user2','user1_turn'))
    return HttpResponse(games_serialized)
	
def get_active_game_list_user(request, pk):
    games = Game.objects.all().filter(Q(outcome=-2) | Q(outcome=-1)).filter(Q(user1=pk) | Q(user2=pk)).order_by('created_date').order_by('created_date')
    games_serialized = serializers.serialize("json", games, fields=('user1','user2','user1_turn'))
    return HttpResponse(games_serialized)
	
