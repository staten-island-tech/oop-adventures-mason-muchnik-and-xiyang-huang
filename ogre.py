class Ogre():
    def __init__(self, hitpoints, speed, inventory):
        self.hitpoints = hitpoints
        self.speed = speed
        self.inventory = inventory

        hitpoints: int = 120
        speed: int =  200
        inventory: str = ["Starter Club"]