from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^newuser/', views.create_user),
    url(r'^$', views.main_page, name='main_page'),
	url(r'^get_username/(?P<pk>\d+)/$', views.get_username, name='get_username'),
    url(r'^get_challenge_list/(?P<pk>\d+)/$', views.get_challenge_list, name='get_challenge_list'),
    url(r'^game/(?P<pk>\d+)/$', views.game_page, name='game_page'),
    url(r'^new_game/(?P<user2pk>\d+)/$', views.new_game, name='new_game'),
    url(r'^get_board_state/(?P<game_id>\d+)/$', views.get_board_state, name='get_board_state'),
    url(r'^change_board_state/(?P<game_id>\d+)/(?P<square>\d+)/$', views.change_board_state, name='change_board_state'),
]