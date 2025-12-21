class Goblin():
    def __init__(self, hitpoints, speed, inventory):
        self.hitpoints = hitpoints
        self.speed = speed
        self.inventory = inventory

        hitpoints: int = 80
        speed: int =  300
        inventory: str = ["Starter Dagger"]