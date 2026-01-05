import random

class Player():
    def __init__(self, race):
        self.race = race
        self.inventory = []

        if race == "Human":
            self.hitpoints = 100
            self.maxhp = 100
            self.speed = 250
            self.inventory.append("Starter Sword")
            
        elif race == "Goblin":
            self.hitpoints = 80
            self.maxhp = 80
            self.speed = 300
            self.inventory.append("Starter Dagger")

        elif race == "Ogre":
            self.hitpoints = 120
            self.maxhp = 120
            self.speed = 200
            self.inventory.append("Starter Club")

    def take_damage(self, enemy):
        attack = random.choice(list(enemy.attacks.keys()))
        damage = enemy.attacks[attack]
        self.hitpoints -= damage
        print(f"Skeleton used {attack} for {damage} damage!")
        return self.hitpoints
    
    def attack(self, enemy):
        for i in john.inventory:
            if i in Weapons["name"]:
                a = Weapons[a]
        enemy.hitpoints -= Weapons[a]["damage"]

class Skeleton():
    def __init__(self):
        self.hitpoints = 10
        self.speed = 180
        self.xp = 5
        self.attacks = {
            "Punch": 5,
            "Bone Throw": 10
        }

    def respawn(self):
        if self.hitpoints <= 0:
            self.hitpoints = 10    

Weapons = [
    {"name": "Starter Sword", "damage": 15},
    {"name": "Wooden Sword", "damage": 25},
    {"name": "Iron Sword", "damage": 40},
    {"name": "Starter Dagger", "damage": 10},
    {"name": "Stone Dagger", "damage": 15},
    {"name": "Short Sword", "damage": 25},
    {"name": "Starter Club", "damage": 30},
    {"name": "Spiked Club", "damage": 40},
    {"name": "Iron Axe", "damage": 60}
]

skeleton = Skeleton()
john = Player("Human")

print(john.hitpoints)
john.take_damage(skeleton)
john.attack(skeleton)