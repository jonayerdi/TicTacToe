from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .forms import PostForm
from .models import Post

def main_page(request):
	users = User.objects.all()
	user_games = Game.objects.filter(user1=request.user.pk | user2=request.user.pk).filter(is_finished=0).order_by('created_date')[:16]
    games = Game.objects.filter(is_finished=0).order_by('created_date')[:16]
    return render(request, 'tictactoe/main_page.html', {'users': users, 'user_games': user_games, 'games': games})
	
def game_page(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'tictactoe/game_page.html', {'game': game})