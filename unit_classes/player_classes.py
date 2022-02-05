from assets.unit_base import Unit



class Mage(Unit):
    def __init__(self):
        self.agility = 5
        self.strength = 5
        self.technique = 15
        self.luck = 5
        self.vitality = 3
        super().__init__(vitality=self.vitality, strength=self.strength, technique=self.technique)
        self.skill_points = 3


class Warrior(Unit):
    def __init__(self):
        self.agility = 8
        self.strength = 15
        self.technique = 5
        self.luck = 8
        self.vitality = 5
        super().__init__(vitality=self.vitality, strength=self.strength, technique=self.technique)
        self.skill_points = 3


class Medic(Unit):
    def __init__(self):
        self.agility = 5
        self.strength = 5
        self.technique = 14
        self.luck = 5
        self.vitality = 4
        super().__init__(vitality=self.vitality, strength=self.strength, technique=self.technique)
        self.skill_points = 3


class Paladin(Unit):
    def __init__(self):
        self.agility = 8
        self.strength = 15
        self.technique = 12
        self.luck = 5
        self.vitality = 6
        super().__init__(vitality=self.vitality, strength=self.strength, technique=self.technique)
        self.skill_points = 3


class Arbalist(Unit):
    def __init__(self):
        self.agility = 15
        self.strength = 13
        self.technique = 8
        self.luck = 10
        self.vitality = 4
        super().__init__(vitality=self.vitality, strength=self.strength, technique=self.technique)
        self.skill_points = 3


