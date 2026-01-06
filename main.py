import random

#game enemies
class Skeleton():
    def __init__(self):
        self.name = "Skeleton"
        self.hitpoints = 10
        self.speed = 180
        self.xp = 5
        self.attacks = {
            "Punch": 5,
            "Bone Throw": 10
        }

    def respawn(self):
        print("You have defeated the Skeleton!")
        self.hitpoints = 10


class Zombie():
    def __init__(self):
        self.name = "Zombie"
        self.hitpoints = 30
        self.speed = 160
        self.xp = 5
        self.attacks = {
            "Punch": 10,
            "Bite": 10
        }

    def respawn(self):
        print("You have defeated the Zombie!")
        self.hitpoints = 30


class Wolves():
    def __init__(self):
        self.name = "Wolves"
        self.hitpoints = 25
        self.speed = 300
        self.xp = 10
        self.attacks = {
            "Bite": 15,
        }

    def respawn(self):
        print("You have defeated the Wolves!")
        self.hitpoints = 25


class BabyTroll():
    def __init__(self):
        self.name = "Baby Troll"
        self.hitpoints = 50
        self.speed = 160
        self.xp = 20
        self.attacks = {
            "Punch": 30,
        }

    def respawn(self):
        print("You have defeated the Baby Troll!")
        self.hitpoints = 50


class Troll():
    def __init__(self):
        self.name = "Troll"
        self.hitpoints = 150
        self.speed = 160
        self.xp = 40
        self.attacks = {
            "Slam": 50,
        }

    def respawn(self):
        print("You have defeated the Troll!")
        self.hitpoints = 150


class ElderTroll():
    def __init__(self):
        self.name = "Elder Troll"
        self.hitpoints = 300
        self.speed = 180
        self.xp = 60
        self.attacks = {
            "Slam": 80,
        }

    def respawn(self):
        print("You have defeated the Elder Troll!")
        self.hitpoints = 300


#game items
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

Armor = [
    {"name": "Leather Armor", "health": 10},
    {"name": "Chainmail Armor", "health": 10, "speed": 20},
    {"name": "Iron Armor", "health": 20, "speed": -20}
]
#start game
racepicker = input("what race do you want to be?\n1. Human\n2. Goblin\n3. Ogre\n").lower().strip()

#player
class Player():
    def __init__(self, race):
        self.race = race
        self.inventory = []

        if race in ("human", "1"):
            self.hitpoints = 100
            self.maxhp = 100
            self.speed = 250
            self.inventory.append("Starter Sword")

        elif race in ("goblin", "2"):
            self.hitpoints = 80
            self.maxhp = 80
            self.speed = 300
            self.inventory.append("Starter Dagger")

        elif race in ("ogre", "3"):
            self.hitpoints = 120
            self.maxhp = 120
            self.speed = 200
            self.inventory.append("Starter Club")

    def take_damage(self, enemy):
        attack = random.choice(list(enemy.attacks.keys()))
        damage = enemy.attacks[attack]
        self.hitpoints -= damage
        self.hitpoints = max(0, self.hitpoints)

        print(f"{enemy.name} used {attack} for {damage} damage!")

    def attack(self, enemy):
        for item in self.inventory:
            for weapon in Weapons:
                if weapon["name"] == item:
                    damage = weapon["damage"]
                    enemy.hitpoints -= damage
                    enemy.hitpoints = max(0, enemy.hitpoints)

                    print(f"John used {item} for {damage} damage!")
                    print(f"{enemy.name} HP: {enemy.hitpoints}")

                    if enemy.hitpoints == 0:
                        enemy.respawn()
                    return

    def show_hp(self):
        print(f"You have {self.hitpoints} HP")


#running game


"""battle test"""
# skeleton = Skeleton()
# john = Player(racepicker)

# print("John HP:", john.hitpoints)
# john.take_damage(skeleton)
# john.show_hp()
# john.attack(skeleton)