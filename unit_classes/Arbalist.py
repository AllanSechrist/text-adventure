from assets.unit_base import Unit


class Arbalist(Unit):
    def __init__(self):
        self.agility = 15
        self.strength = 13
        self.technique = 8
        self.luck = 10
        self.vitality = 4
        super().__init__(vitality=self.vitality, strength=self.strength, technique=self.technique)
        self.skill_points = 3
        self.skills = []
        self.name = "Arbalist"


