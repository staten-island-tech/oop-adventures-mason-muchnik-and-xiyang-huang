class Human():
    def __init__(self, hitpoints, speed, inventory):
        self.hitpoints = hitpoints
        self.speed = speed
        self.inventory = inventory

        hitpoints: int = 100
        speed: int =  250
        inventory: str = ["Starter Sword"]