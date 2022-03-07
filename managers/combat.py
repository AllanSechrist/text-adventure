from unit_classes.floor_one_enemies import *

class CombatManager():
    def __init__(self, player_party):
        self.enemies = [Rat(), Rat()]
        self.player_party = player_party
    

    def combat(self):
        print("You are under attack!")
        print(" ")
        self.player_attack_phase()
        return True


    def get_target(self):
        for i, enemy in enumerate(self.enemies):
            print(f"{i}: {enemy.name}")
        target = int(input("Please select a target by number: "))
        return target


    def enemy_attack_phase(self):
        pass


    def player_attack_phase(self):
        for unit in self.player_party:
            unit.defending = False
        index = 0
        done = False
        while not done:
            print(' ')
            print("Attack")
            print("Defend")
            print("Skill")
            print("Escape")
            print(' ')
            print(f'{self.player_party[index].name} HP:{self.player_party[index].hp}/{self.player_party[index].max_hp}')
            print(f'{self.player_party[index].name} TP:{self.player_party[index].tp}/{self.player_party[index].max_tp}')
            player_input = input(f"Please select an action for {self.player_party[index].name}: ").upper()

            if player_input == "ATTACK" or player_input == "A":
                target = self.get_target()
                if target < len(self.enemies):
                    print(f"{self.player_party[index].name} attacks {self.enemies[target].name}")
                    self.player_party[index].basic_attack(self.enemies[target])
                    if self.enemies[target].hp <= 0:
                        print(f'{self.enemies[target].name} has died.')
                        del self.enemies[target]
                    index += 1
                else:
                    print("You must enter a valid input!")
                
            elif player_input == "DEFEND" or player_input == "D":
                self.player_party[index].defending = True
                print(f"{self.player_party[index].name} is defending!")
                index += 1

            elif player_input == "SKILL" or player_input == "S":
                target = self.get_target()
                if target < len(self.enemies):
                    self.player_party[index].cast(self.enemies[target])
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

            if len(self.enemies) == 0:
                done = True

