from assets.unit_base import Unit
from random import randint

class Rat(Unit):
    def __init__(self):
        self.agility = 3
        self.strength = 8
        self.technique = 0
        self.luck = 3
        self.vitality = 3
        super().__init__(vitality=self.vitality, strength=self.strength, technique=self.technique)
        self.name = 'Rat'


class Mole(Unit):
    def __init__(self):
        self.agility = 3
        self.strength = 15
        self.technique = 0
        self.luck = 3
        self.vitality = 5
        super().__init__(vitality=self.vitality, strength=self.strength, technique=self.technique)
        self.name = 'Mole'


class Beetle(Unit):
    def __init__(self):
        self.agility = 4
        self.strength = 10
        self.technique = 0
        self.luck = 3
        self.vitality = 4
        super().__init__(vitality=self.vitality, strength=self.strength, technique=self.technique)
        self.name = 'Beetle'



def generate_enemy():
    roll = randint(0, 100)
    if roll < 50:
        return Rat()
    elif roll >= 50 and roll <= 80:
        return Mole()
    else:
        return Beetle()