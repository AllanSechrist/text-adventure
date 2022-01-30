from assets.map import Map
from managers.player import PlayerManager


class GameManager():
    def __init__(self):
        self.map = Map(10)
        self.player = PlayerManager()


    def update_player_position(self):
        self.map.move_player()


    def map_loop(self):
        done = False
        while not done:
            self.map.draw_board(player_y=self.player.y, player_x=self.player.x)
            done = self.player.move_player()

