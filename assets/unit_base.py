import random

class Unit():
    def __init__(self, vitality, strength, technique):
        # self.speed = 0
        # self.strength = 0
        # self.technique = 0
        # self.luck = 0
        # self.vitality = 0
        self.max_hp = vitality * 5
        self.hp = self.max_hp
        self.attack = strength # + self.weapon.attack
        self.defence = vitality # + self.armor_total
        self.max_tp = technique * 3
        self.tp = self.max_tp
        self.defending = False

        self.buff_list = []
        self.debuff_list = []

        self.head_bound = False
        self.arms_bound = False
        self.legs_bound = False
        self.name = ''


    def roll(self):
        roll = random.randint(0, 100)
        return roll
    

    def basic_attack(self, target):
        roll = self.roll()
        if roll < target.agility:
            print("miss")
        else:
            damage = self.attack - target.defence
            target.hit(damage)
            

    def hit(self, damage):
        if self.defending:
            self.hp = self.hp - int(damage / 2)
            print(f"{self.name} took {str(damage)} damage!")
        else:
            self.hp = self.hp - damage
            print(f"{self.name} took {str(damage)} damage!")

    def defend(self):
        self.defending = True