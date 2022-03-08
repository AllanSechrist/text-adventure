from unit_classes.player_classes.Mage import Mage
from unit_classes.player_classes.Warrior import Warrior
from unit_classes.player_classes.Paladin import Paladin
from unit_classes.player_classes.Medic import Medic
from unit_classes.player_classes.Arbalist import Arbalist
from random import randint


class PlayerManager():
    def __init__(self):
        self.x = 0
        self.y = 0
    
        self.previous_x = 0
        self.previous_y = 0

        # self.front_row = [Paladin()]
        # self.back_row = [Mage()]

        self.party = [Mage(), Paladin(), Arbalist()]

        self.encounter_meter = 0 # once this value reaches 100, create an encounter.


    def move_player(self):
        user_choice = input("Please enter a direction(N,E,S,W): ").upper()

        self.previous_x = self.x
        self.previous_y = self.y

        if user_choice == "N":
            self.y = self.y - 1
        elif user_choice == "E":
            self.x = self.x + 1
        elif user_choice == "S":
            self.y = self.y + 1
        elif user_choice == "W":
            self.x = self.x - 1
        elif user_choice == "Q":
            return True
        
        if self.y < 0 or self.x < 0: 
            self.x = self.previous_x
            self.y = self.previous_y
            print("You have hit a wall!")
        else:
            self.increase_encounter_meter()
    

    def increase_encounter_meter(self):
        roll = randint(1, 15)
        self.encounter_meter += roll
        print(f'Encounter: {self.encounter_meter}/100')


