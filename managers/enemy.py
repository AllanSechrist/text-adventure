from unit_classes.floor_one_enemies import *
from random import choice, randint


class EnemyManager():
    def __init__(self, player):
        self.encounter_meter = 0


    def roll(self):
        roll = randint(0, 100)
        return roll


    def floor_one_enemy_groups():
        groups = {
            0 : [Rat(), Rat(), Rat()],
            1 : [Rat(), Beetle()],
            2 : [Mole(), Rat()],
            3 : [Mole(), Beetle()],
        }

    
    def generate_enemy_list(self, floor):
        enemy_group = []
        roll = self.roll()
