from unit_base import Unit

class Mage(Unit):
    def __init__(self):
        super().__init__()
        self.hp = 30
        self.attack = 5
        self.defence = 0
        self.speed = 0


class Warrior(Unit):
    def __init__(self):
        super().__init__()
        self.hp = 50
        self.attack = 5
        self.defence = 5
        self.speed = 0


class Medic(Unit):
    def __init__(self):
        super().__init__()
        self.hp = 30
        self.attack = 5
        self.defence = 0
        self.speed = 0


class Paladin(Unit):
    def __init__(self):
        super().__init__()
        self.hp = 60
        self.attack = 5
        self.defence = 10
        self.speed = 0

