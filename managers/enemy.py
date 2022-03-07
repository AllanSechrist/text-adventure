from unit_classes.floor_one_enemies import *
from random import choice, randint


class EnemyManager():
    def __init__(self, player):
        self.encounter_meter = 0
        self.player_floor = 0


    def roll(self):
        roll = randint(0, 100)
        return roll

   
    def generate_enemy_list(self):
        enemy_group = []
        roll = self.roll()
