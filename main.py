from Player import *
from enemies import *
from items.armour import *
#__________________________________________________________________________________________________________________________________


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