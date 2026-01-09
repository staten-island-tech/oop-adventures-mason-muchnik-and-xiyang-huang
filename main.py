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
    "Skeleton", 10, 180, 20,
    {"Punch": 5, "Bone Throw": 10}
)

Zombie = Enemy(
    "Zombie", 30, 160, 20,
    {"Punch": 10, "Bite": 10}
)

Wolf = Enemy(
    "Wolf", 25, 300, 20,
    {"Bite": 15}
)

BabyTroll = Enemy(
    "Baby Troll", 50, 160, 60,
    {"Punch": 30}
)

Troll = Enemy(
    "Troll", 150, 160, 80,
    {"Slam": 50}
)

ElderTroll = Enemy(
    "Elder Troll", 300, 180, 100,
    {"Slam": 80}
)
DemonLord = Enemy(
    "Demon Lord", 500, 220, 150,
    {"Hell Slash": 70, "Inferno": 120}
)

VoidReaper = Enemy(
    "Void Reaper", 650, 240, 200,
    {"Void Cleave": 90, "Soul Rip": 140}
)

AncientDragon = Enemy(
    "Ancient Dragon", 900, 200, 300,
    {"Fire Breath": 160, "Tail Smash": 120, "Claw Rend": 100}
)

ElderLich = Enemy(
    "Elder Lich", 550, 260, 250,
    {"Death Bolt": 110, "Life Drain": 140}
)

TitanOfOblivion = Enemy(
    "Titan of Oblivion", 1200, 180, 400,
    {"World Crusher": 200, "Seismic Slam": 160}
)

starterenemies = [Skeleton, Zombie, Wolf]
midenemies = [BabyTroll, Troll, ElderTroll]
endenemies = [DemonLord, VoidReaper, AncientDragon, ElderLich, TitanOfOblivion]

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
        weapon_name = self.inventory[0]
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
        
#encoutners

class Encounter:
    def play(self, player):
        alive = True
        while alive == True:
            if player.level < 10:
                enemy = random.choice(starterenemies)

            elif player.level >= 10 and player.level < 20:
                enemy = random.choice(midenemies)


            if enemy.name == Skeleton:
                print("\nyou've wandered into a graveyard... what in the shit is that???!?!?!")
            elif enemy.name == Zombie:
                print("\nnights quickly approaching and you see a cave you could rest in.")
                print("you hear groans from behind you...")
            elif enemy.name == Wolf:
                print("\nyou walk into a forest.")
                print("ur exhausted and rest against a large tree")
                print("you hear a branch snap near you...")
            elif enemy.name == BabyTroll:
                print("\nphew! you survived that last thing...")
                print("nights approaching and you see a cave you could rest in.")
                print("you hear a slight tremor deeper in the cave...")
            elif enemy.name == Troll:
                print("\nyou stumble into a unusual forest with monstrous trees.")
                print("ur exhausted and rest against a large rock")
                print("an apple suddenly drops on ur head... then more start dropping form the tree")
                print("you feel the ground shake...")
            elif enemy.name == ElderTroll:
                print("\nyou stumble into a unusual forest with monstrous trees.")
                print("ur exhausted and rest against a large rock")
                print("suddenly a huge shadow appears from above you")

            if enemy.hitpoints > 0:
                print(f"\nA {enemy.name} appears!")

            while player.hitpoints > 0 and enemy.hitpoints > 0:
                player.take_damage(enemy)

                if player.hitpoints <= 0:
                    alive = False
                    break

                turn = input("what do you want do to?\n1. flee |2. attack |:").lower().strip()

                if turn in ("1", "flee") and player.speed > enemy.speed:
                    player.flee()

                elif turn in ("2", "attack"):
                    player.attack(enemy)

                else:
                    print("you failed to flee slow fart!")
                    player.take_damage(enemy)


#starts game
LORE = """
Long ago, the lands of xiyangvalley were whole and peaceful.
That peace shattered when ancient creatures crawled from the deep forests
and forgotten caves.

Skeletons wander cursed battlefields.
Zombies rise where plague once spread.
Wolves hunt in packs beneath blood-red moons.
And deep in the mountains, Trolls awaken from their slumber.

The Elder Troll watches from the shadows,
waiting for a warrior foolish or brave enough to challenge fate.

You are one of the few who still stand.
Your race will shape your destiny.
Your blade will decide your legend.

Survive.
Fight.
And carve your name into history.
"""

racepicker = input(
    "choose your race!\n"
    "1. Human\n"
    "2. Goblin\n"
    "3. Ogre\n"
).lower().strip()

player = Player(racepicker)
encounter = Encounter()

print(LORE)
input("\nPress Enter to begin your journey...")
alive = True
while alive:
    alive = encounter.play(player)
    # player.show_stats()