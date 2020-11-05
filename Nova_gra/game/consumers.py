from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.db import database_sync_to_async
from .models import Game
from player.models import Player

class GameEventsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        game_id = (self.scope['url_route']['kwargs']['id'])
        self.game = await self.get_game(id=game_id)
        self.room_group_name = self.game.name


        await (self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    @database_sync_to_async
    def get_game(self,id):
        return Game.objects.get(pk=id)

    @database_sync_to_async
    def get_player(self, usr):
        return Player.objects.get(nick=usr)

    @database_sync_to_async
    def get_game_is_played(self, game):
        return game.is_played

    @database_sync_to_async
    def get_player_in_game(self,player):
        return player.in_game

    @database_sync_to_async
    def add_player_to_game(self, player, game):
        return game.who_is_ready.add(player)

    @database_sync_to_async
    def remove_player_from_game(self, player, game):
        return game.who_is_ready.remove(player)

    @database_sync_to_async
    def set_player_game_status_ready(self, player):
        player.set_player_in_game()

    @database_sync_to_async
    def set_player_game_status_off(self, player):
        player.set_player_leave_game()

    async def receive(self, text_data):

        """
        if text_data == "klik":
            self.counter.klik +=1
        elif text_data == "klak":
            self.counter.key += 1
            """
        game = self.game
        action = message['action']
        game.player = await self.get_player(message['player'])
        player = game.player
        game.is_played = await self.get_game_is_played(game)
        player.in_game = await self.get_player_in_game(player)

        if action=="ready":
            if not game.is_played and not player.in_game:  #and  player not in game.players_ready
                #if game.how_many_players_ready < game.max_players:
                await self.add_player_to_game(player, game)   #adds_to_who_is_ready
                await self.set_player_game_status_ready(player) #player.in game
            elif not game.is_played and player.in_game:
                await self.remove_player_from_game(player, game)
                await self.set_player_game_status_off(player)

        elif action=="start":
            print("Starto!")
        await database_sync_to_async(game.save)()
        await database_sync_to_async(player.save)()
        message = json.loads(text_data)
        #tutaj trzeba wyslac json ze stanem
        await (self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'game_message',
                'message': message,
            }
        )

    async def game_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message,
        }))

    async def disconnect(self, close_code):
        await (self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        await self.close()
