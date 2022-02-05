from assets.unit_base import Unit


class Rat(Unit):
    def __init__(self):
        self.agility = 3
        self.strength = 8
        self.technique = 0
        self.luck = 3
        self.vitality = 3
        super().__init__(vitality=self.vitality, strength=self.strength, technique=self.technique)


class Mole(Unit):
    def __init__(self):
        self.agility = 3
        self.strength = 15
        self.technique = 0
        self.luck = 3
        self.vitality = 5
        super().__init__(vitality=self.vitality, strength=self.strength, technique=self.technique)


class Beetle(Unit):
    def __init__(self):
        self.agility = 4
        self.strength = 10
        self.technique = 0
        self.luck = 3
        self.vitality = 4
        super().__init__(vitality=self.vitality, strength=self.strength, technique=self.technique)
