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
        self.skills = [Fire(), Ice(), Lightning()]
        self.name = 'Mage'

    
    def cast(self, target):
        done = False
        while not done:
            print(' ') 
            for index, skill in enumerate(self.skills):
                print(f'{index}: {skill.name}')
            selected_skill = int(input("Please select a skill by number: "))
            if selected_skill < len(self.skills):
                casted_skill = self.skills[selected_skill]
                print(' ')
                print(f"{self.name} casts {casted_skill.name} on {target.name}!")
                casted_skill.damage(target, self.roll(), self.technique)
                done = True
            else:
                print('Please make a valid input')
            
            

