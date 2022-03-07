from assets.unit_base import Unit


class Warrior(Unit):
    def __init__(self):
        self.agility = 8
        self.strength = 15
        self.technique = 5
        self.luck = 8
        self.vitality = 5
        super().__init__(vitality=self.vitality, strength=self.strength, technique=self.technique)
        self.skill_points = 3
        self.skills = []
        self.name = 'Warrior'



