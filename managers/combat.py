from unit_classes.enemies import *

class CombatManager():
    def __init__(self, player_party):
        self.enemies = [Rat(), Rat()]
        self.player_party = player_party
    

    def combat(self):
        print("You are under attack!")
        print(" ")
        self.player_attack_phase()
        return True

    def player_attack_phase(self):
        for unit in self.player_party:
            unit.defending = False

        index = 0
        done = False
        while not done:
            print("Attack")
            print("Defend")
            print("Skill")
            print("Escape")
            player_input = input(f"Please select an action for {self.player_party[index].name}: ").upper()

            if player_input == "ATTACK" or player_input == "A":
                for enemy in range(len(self.enemies)):
                    print(f"{enemy}: {self.enemies[enemy].name}")
                target = int(input("Please select a target by number: ")) # for testing
                if target < len(self.enemies):
                    print(f"{self.player_party[index].name} attacks {self.enemies[enemy].name}")
                    self.player_party[index].basic_attack(self.enemies[enemy])
                    
                    index += 1
                else:
                    print("You must enter a valid input!")
            elif player_input == "DEFEND" or player_input == "D":
                self.player_party[index].defending = True
                print(f"{self.player_party[index].name} is defending!")
                index += 1

            elif player_input == "SKILL" or player_input == "S":
                print("Skill to come at a later date!")
                index += 1

            elif player_input == "ESCAPE" or player_input == "E":
                escape_roll = self.player_party[index].roll()
                if escape_roll > 5:
                    print("You run away!")
                    done = True
                else:
                    print("You Fail to run!")
                    index += 1
            else:
                print("You must enter a valid command!")

            if index > len(self.player_party)- 1:
                done = True

