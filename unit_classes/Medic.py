from assets.unit_base import Unit


class Medic(Unit):
    def __init__(self):
        self.agility = 5
        self.strength = 5
        self.technique = 14
        self.luck = 5
        self.vitality = 4
        super().__init__(vitality=self.vitality, strength=self.strength, technique=self.technique)
        self.skill_points = 3
        self.skills = []
        self.name = "Medic"



