from django.test import TestCase, Client
from django.urls import reverse, resolve
from game.models import Game
from player.models import Player
from django.contrib.auth.models import User


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.user = User.objects.create_user(username='testuser2', password='12345')
        self.client.login(username='testuser', password='12345')


    def test_authorisation(self):

        self.client.logout()
        game = Game.objects.create(name='empty', host='dottore', is_played=False, max_players=4, players_ready=0)
        self.join_url_empty = reverse('game_join', args=[game.id])
        response = self.client.get(self.join_url_empty, follow=True)

        self.assertEqual(response.request['PATH_INFO'],'/player/login')


    def test_join_empty_room(self):

        game = Game.objects.create(name='empty',host='dottore',is_played=False,max_players=4,players_ready=0)
        self.join_url_empty = reverse('game_join', args=[game.id])
        response = self.client.get(self.join_url_empty, follow=True)

        self.assertEquals(response.request['PATH_INFO'],'/game/1/')



# Gracz może tworzyć dowolną liczbę pokoi.

#Gracz może tworzyć dowolną liczbę pokoi.

#Gracz może dołączyć do pokoju.

# Gracz, który założył pokój/grę może usunąć go, jeżeli nie ma w nim innych graczy lub gdy gra nie jest aktywna.

# W pokoju może być maksymalnie 4 graczy.

# Każdy może zobaczyć listę wszystkich pokojów, ale wejść można do niepełnego.

# Twórca pokoju musi podać jego nazwę na etapie tworzenia pokoju.


