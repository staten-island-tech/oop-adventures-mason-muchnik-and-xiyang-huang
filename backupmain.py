# let it be known that Xiyang sucks at writing code that is clear and organized for others. Therefore this file was created to unsure that I, Mason Muchnik
#In the case that I screw things up there are back ups for me to jsut copy and paste.



from Player import *


class Encounter:
    def play(self, player):
        alive = True
        if alive == True:
            if player.level < 10:
                enemy = random.choice(starterenemies)

            elif player.level >= 10 and player.level < 20:
                enemy = random.choice(midenemies)

            if enemy == Skeleton:
                print("\nyou've wandered into a graveyard... what in the shit is that?!")
            elif enemy == Zombie:
                print("\nnights quickly approaching and you see a cave you could rest in.")
                print("you hear groans from behind you...")
            elif enemy == Wolf:
                print("\nyou walk into a forest.")
                print("ur exhausted and rest against a large tree")
                print("you hear a branch snap near you...")
            elif enemy == BabyTroll:
                print("\nphew! you survived that last thing...")
                print("nights approaching and you see a cave you could rest in.")
                print("you hear a slight tremor deeper in the cave...")
            elif enemy == Troll:
                print("\nyou stumble into a unusual forest with monstrous trees.")
                print("ur exhausted and rest against a large rock")
                print("an apple suddenly drops on ur head... then more start dropping form the tree")
                print("you feel the ground shake...")
            elif enemy == ElderTroll:
                print("\nyou stumble into a unusual forest with monstrous trees.")
                print("ur exhausted and rest against a large rock")
                print("suddenly a huge shadow appears from above you")

            enemy.respawn()

            if enemy.hitpoints > 0:
                print(f"\nA {enemy.name} appears!")

            while player.hitpoints > 0 and enemy.hitpoints > 0:
                player.take_damage(enemy)

                if player.hitpoints <= 0:
                    alive = False
                    break

                turn = input("what do you want do to?\n1. flee |2. attack |3. open inventory |:").lower().strip()

                if turn in ("1", "flee") and player.speed > enemy.speed:
                    player.flee()

                elif turn in ("2", "attack"):
                    player.attack(enemy)

                elif turn in ("3", "open inventory"):
                    print("\n in ur inventory u have:")
                    print(player.inventory)
                    if "Heal Potion" in player.inventory:
                        print(f"you have a heal potion.")
                        use = input(f"\n1. use |2. close inventory |:").lower().strip()
                        if use in ("1", "use"):
                            print("you have used heal potion and gained 40 hp")
                            player.hitpoints += 40
                            print(f"your hp is now {player.hitpoints}")
                    
                    elif "Apple" in player.inventory:
                        print("u have an apple")
                        use = input(f"\n1. use |2. close inventory |:").lower().strip()
                        if use in ("1", "use"):
                            print("you have ate an apple and gained 10 hp")
                            player.hitpoints += 10
                            print(f"your hp is now {player.hitpoints}")
                    


                elif turn in ("1", "flee") and player.speed <= enemy.speed:
                    print("you failed to flee slow fart!")
                    player.take_damage(enemy)

    def inbetween(self):
        print("\nphew! you survived the battle")
        e = random.randint(1,3)

        if e == 1:
            print("\nyou have found a tree")
            chop = input("1. chop |2. leave |:").lower().strip()
            if chop in ("1", "chop"):
                print("u have chopped the tree down. you have obtained 2 wood and 3 apples")
                player.inventory.extend(["Wood", "Wood", "Apple", "Apple", "Apple"])

        elif e == 2:
            print("\nyou have found a cave")
            cave = input("1. enter |2. leave |:").lower().strip()
            if cave in ("1", "enter"):
                print("\nu have entered the cave. you find iron ore")
                mine = input("1. mine |2. leave |:").lower().strip()
                if mine in ("1", "mine"):
                    print("\nu have mined the iron. u have obtained 2 pieces of iron")
                    player.inventory.append("Iron")
                else:
                    print("why would u leave free iron")
            else:
                print("what a baby")

        elif e == 3 and "Iron Sword" not in player.inventory and "Iron Dagger" not in player.inventory and "Iron Club" not in player.inventory:
            print("\nyou have found a village and is talking to the blacksmith")
            print("Blacksmith: if you trade me 1 piece of iron ill give u an iron weapon")
            trade = input("1. trade |2. leave |:").lower().strip()
            if trade in ("1", "trade") and "Iron" in player.inventory:
                print("u are now trading with the blacksmith")
                if player.race == "Human":
                    print("you have obtained an Iron Sword")
                    index = player.inventory.index("Starter Sword")
                    player.inventory[index] = "Iron Sword"

                if player.race == "Goblin":
                    print("you have obtained an Iron Dagger")
                    index = player.inventory.index("Starter Dagger")
                    player.inventory[index] = "Iron Dagger"

                if player.race == "Ogre":
                    print("you have obtained an Iron Club")
                    index = player.inventory.index("Starter Club")
                    player.inventory[index] = "Iron Club"

            else:
                print("u dont have any iron fat scammer")
            
        player.hitpoints += 10
        print("ur now kinda well rested. u have gained 10 hp.\nhopefully there isnt another battle")

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
    encounter.play(player)
    if player.hitpoints > 0:
        encounter.inbetween()
    else:
        player.show_stats()