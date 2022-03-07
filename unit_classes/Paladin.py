from assets.unit_base import Unit


class Paladin(Unit):
    def __init__(self):
        self.agility = 8
        self.strength = 15
        self.technique = 12
        self.luck = 5
        self.vitality = 6
        super().__init__(vitality=self.vitality, strength=self.strength, technique=self.technique)
        self.skill_points = 3
        self.skills = []
        self.name = "Paladin"


