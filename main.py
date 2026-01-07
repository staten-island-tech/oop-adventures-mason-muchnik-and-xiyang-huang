import random

#enmies
class Enemy:
    def __init__(self, name, hp, speed, xp, attacks):
        self.name = name
        self.maxhp = hp
        self.hitpoints = hp
        self.speed = speed
        self.xp = xp
        self.attacks = attacks

    def respawn(self):
        print(f"You have defeated the {self.name}!")
        self.hitpoints = self.maxhp


Skeleton = Enemy(
    "Skeleton", 10, 180, 5,
    {"Punch": 5, "Bone Throw": 10}
)

Zombie = Enemy(
    "Zombie", 30, 160, 5,
    {"Punch": 10, "Bite": 10}
)

Wolf = Enemy(
    "Wolves", 25, 300, 10,
    {"Bite": 15}
)

BabyTroll = Enemy(
    "Baby Troll", 50, 160, 20,
    {"Punch": 30}
)

Troll = Enemy(
    "Troll", 150, 160, 40,
    {"Slam": 50}
)

ElderTroll = Enemy(
    "Elder Troll", 300, 180, 60,
    {"Slam": 80}
)

enemies = [Skeleton, Zombie, Wolf, BabyTroll, Troll, ElderTroll]

#itemsf

Weapons = {
    "Starter Sword": 15,
    "Wooden Sword": 25,
    "Iron Sword": 40,
    "Starter Dagger": 10,
    "Stone Dagger": 15,
    "Short Sword": 25,
    "Starter Club": 30,
    "Spiked Club": 40,
    "Iron Axe": 60
}
Armor = [
    {"name": "Leather Armor", "health": 10},
    {"name": "Chainmail Armor", "health": 10, "speed": 20},
    {"name": "Iron Armor", "health": 20, "speed": -20}
]
#playere

class Player:
    def __init__(self, race):
        self.inventory = []
        self.level = 1
        self.experience = 0
        self.kills = 0

        if race in ("human", "1"):
            self.race = "Human"
            self.maxhp = 100
            self.speed = 250
            self.inventory.append("Starter Sword")

        elif race in ("goblin", "2"):
            self.race = "Goblin"
            self.maxhp = 80
            self.speed = 300
            self.inventory.append("Starter Dagger")

        elif race in ("ogre", "3"):
            self.race = "Ogre"
            self.maxhp = 120
            self.speed = 200
            self.inventory.append("Starter Club")

        else:
            raise ValueError("Invalid race")

        self.hitpoints = self.maxhp

    def take_damage(self, enemy):
        attack = random.choice(list(enemy.attacks))
        damage = enemy.attacks[attack]
        self.hitpoints = max(0, self.hitpoints - damage)
        print(f"{enemy.name} used {attack} for {damage} damage!")

    def attack(self, enemy):
        weapon_name = self.inventory[0]
        damage = Weapons[weapon_name]

        enemy.hitpoints = max(0, enemy.hitpoints - damage)
        print(f"You used {weapon_name} for {damage} damage!")
        print(f"{enemy.name} HP: {enemy.hitpoints}")

        if enemy.hitpoints == 0:
            enemy.respawn()
            self.kills += 1
            self.experience += enemy.xp
            self.check_level_up()

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
        
#encoutners

class Encounter:
    def play(self, player):
        enemy = random.choice(enemies)
        print(f"\nA {enemy.name} appears!")

        while enemy.hitpoints > 0 and player.hitpoints > 0:
            player.take_damage(enemy)
            turn = input(f"what do you want to do?\n1. flee\n2. attack").lower().strip()
            if turn in ("1", "flee"):
                player.flee()
                enemy.hitpoints == 0

            elif turn == ("2", "attack"):
                player.attack(enemy)

        if player.hitpoints == 0:
            print("You have died.")
            return False

        return True

#starts game

racepicker = input(
    "choose your race player!\n"
    "1. Human\n"
    "2. Goblin\n"
    "3. Ogre\n"
).lower().strip()

player = Player(racepicker)
encounter = Encounter()

print("\nWelcome to super cool xiyangs game!")

alive = True
while alive:
    alive = encounter.play(player)
    player.show_stats()