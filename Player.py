# class Human():
#     def __init__(self, hitpoints, speed, inventory):
#         self.hitpoints = hitpoints
#         self.speed = speed
#         self.inventory = inventory

#         hitpoints = 100
#         speed = 250
#         inventory = ["Starter Sword"]

# class Goblin():
#     def __init__(self, hitpoints, speed, inventory):
#         self.hitpoints = hitpoints
#         self.speed = speed
#         self.inventory = inventory

#         hitpoints = 80
#         speed = 300
#         inventory = ["Starter Dagger"]

# class Ogre():
#     def __init__(self, hitpoints, speed, inventory):
#         self.hitpoints = hitpoints
#         self.speed = speed
#         self.inventory = inventory

#         hitpoints = 120
#         speed = 200
#         inventory = ["Starter Club"]

class Player():
    def __init__(self, race, hitpoints, speed, inventory):
        self.race = race
        #race
        if race == "Human":
            hitpoints = 100
            speed = 250
            inventory.append("Starter Sword")
        elif race == "Goblin":
            hitpoints = 80
            speed = 300
            inventory.append("Starter Dagger")
        elif race == "Ogre":
            hitpoints = 120
            speed = 200
            inventory.append("Starter Club")

        self.hitpoints = hitpoints
        self.speed = speed
        self.inventory = inventory

        inventory = []