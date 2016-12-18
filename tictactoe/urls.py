from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^newuser/', views.create_user),
    url(r'^$', views.main_page, name='main_page'),
	url(r'^game/(?P<pk>\d+)/$', views.game_page, name='game_page'),
	url(r'^get_board_state/(?P<game_id>\d+)/$', views.board_state, name='board_state'),
]