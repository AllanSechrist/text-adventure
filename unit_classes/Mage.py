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


