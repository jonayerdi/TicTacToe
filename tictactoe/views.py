from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .forms import PostForm
from .models import Post

def main_page(request):
	users = User.objects.all()
    games = Game.objects.filter(is_finished=0).order_by('created_date')[:10]
    return render(request, 'tictactoe/main_page.html', {'users': users, 'games': games})
	
def game_page(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'tictactoe/game_page.html', {'game': game})