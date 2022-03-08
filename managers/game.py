from assets.map import Map
from managers.player import PlayerManager
from managers.combat import CombatManager



class GameManager():
    def __init__(self):
        self.map = Map(10)
        self.player = PlayerManager()
        self.combat_manager = CombatManager(player_party=self.player.party)


    def map_loop(self):
        done = False
        while not done:
            self.map.draw_board(player_y=self.player.y, player_x=self.player.x)
            done = self.player.move_player()


    def combat_loop(self):
        done = False
        while not done:
            done = self.combat_manager.combat()