import random
from enemies import *
from weapons import *
from armor import *

class Player:
    def __init__(self, race):
        self.inventory = ["Heal Potion", "Wooden Axe", "Wooden Pickaxe"]
        self.level = 0
        self.experience = 0
        self.kills = 0

        if race in ("human", "1"):
            self.race = "Human"
            self.maxhp = 100
            self.speed = 200
            self.inventory.append("Starter Sword")

        elif race in ("goblin", "2"):
            self.race = "Goblin"
            self.maxhp = 80
            self.speed = 250
            self.inventory.append("Starter Dagger")

        elif race in ("ogre", "3"):
            self.race = "Ogre"
            self.maxhp = 120
            self.speed = 150
            self.inventory.append("Starter Club")

        else:
            raise ValueError("Invalid race")

        self.hitpoints = self.maxhp

    def take_damage(self, enemy):
        attack = random.choice(list(enemy.attacks))
        damage = enemy.attacks[attack]
        self.hitpoints = max(0, self.hitpoints - damage)
        print(f"{enemy.name} used {attack} for {damage} damage!")
        if self.hitpoints <= 0:
            print("yuo died")
        elif self.hitpoints > 0:
            print(f"you have {self.hitpoints} hp left")

    def attack(self, enemy):
        weapon_name = self.inventory[3]
        damage = Weapons[weapon_name]

        enemy.hitpoints = max(0, enemy.hitpoints - damage)
        print(f"\nYou used {weapon_name} for {damage} damage!")
        print(f"{enemy.name} current HP: {enemy.hitpoints}")

        if enemy.hitpoints <= 0:
            self.kills += 1
            self.experience += enemy.xp
            self.check_level_up()
            print("you have defeated the enemy!")

    def check_level_up(self):
        while self.experience >= 100:
            self.experience -= 100
            self.level += 1
            self.maxhp += 10
            self.hitpoints = self.maxhp
            print("you have leveled up")

    def show_stats(self):
        print(f"\nRace: {self.race}")
        print(f"HP: {self.hitpoints}/{self.maxhp}")
        print(f"Level: {self.level}")
        print(f"XP: {self.experience}")
        print(f"Kills: {self.kills}")

    def flee(self):
        print("you have fled from the battle!")
        print("What a wuss!")
        