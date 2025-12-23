class Player:
    def __init__(self, race):
        self.race = race
        self.inventory = []

        if race == "Human":
            self.hitpoints = 100
            self.speed = 250
            self.inventory.append("Starter Sword")
            
        elif race == "Goblin":
            self.hitpoints = 80
            self.speed = 300
            self.inventory.append("Starter Dagger")

        elif race == "Ogre":
            self.hitpoints = 120
            self.speed = 200
            self.inventory.append("Starter Club")

#starts game
#create gui to start game
cc = input("Character Creation: \n1. Human \n2. Goblin\n3. Ogre\n\nWhat race do you want to be?").lower().strip()

if cc == "human":
    test = Player("Human")
    print(test.race)
elif cc == "goblin":
    test = Player("Goblin")
    print(test.race)
elif cc == "ogre":
    test = Player("Ogre")
    print(f"Your race is: {test.race}")
else:
    print("That is not an option.")