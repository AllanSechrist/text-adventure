from assets.skill_base import Skill


class Fire(Skill):
    def __init__(self):
        super().__init__(1.8, 5, 'offensive')
        self.element = "Fire"
        self.skill_level = 0
        self.name = "Fire"


class Ice(Skill):
    def __init__(self):
        super().__init__(1.8, 5, 'offensive')
        self.element = "Ice"
        self.skill_level = 0
        self.name = "Ice"


class Lightning(Skill):
    def __init__(self):
        super().__init__(1.8, 5, 'offensive')
        self.element = "Lightning"
        self.skill_level = 0
        self.name = "Lightning"