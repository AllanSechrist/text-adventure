from assets.unit_base import Unit
from assets.mage_skills import *


class Mage(Unit):
    def __init__(self):
        self.agility = 5
        self.strength = 5
        self.technique = 15
        self.luck = 5
        self.vitality = 3
        super().__init__(vitality=self.vitality, strength=self.strength, technique=self.technique)
        self.skill_points = 3
        self.skills = {'FIRE': Fire(), 'ICE': Ice(), 'LIGHTNING': Lightning()}
        self.name = 'Mage'

    
    def cast(self, target):
        done = False
        for key, skill in self.skills.items():
            print(f'{skill.name}')
        while not done:
            player_input = input("Please select a skill: ").upper()
            if player_input in self.skills:
                print(f"{self.name} casts {skill.name} on {target.name}!")
                skill.damage(target, self.roll(), self.technique)
                done = True
            else:
                print("Please make a valid input")
            # for skill in self.skills:
            #     if player_input == skill.name.upper():
            #         print(f"{self.name} casts {skill.name} on {target.name}!")
            #         skill.damage(target, self.roll(), self.technique)
            #         done = True
            #         return
            #     else:
            #         print('Please make a valid input')


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


