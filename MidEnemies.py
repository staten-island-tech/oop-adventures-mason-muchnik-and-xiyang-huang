class Troll():
    def __init__(self, hitpoints, speed, xp, attacks):
        self.hitpoints = hitpoints
        self.speed = speed
        self.xp = xp
        self.attacks = attacks

        hitpoints = 200
        speed = 160
        xp = 40
        attacks = {
            "Slam": 50,
        }

class ElderTroll():
    def __init__(self, hitpoints, speed, xp, attacks):
        self.hitpoints = hitpoints
        self.speed = speed
        self.xp = xp
        self.attacks = attacks

        hitpoints = 300
        speed = 180
        xp = 60
        attacks = {
            "Slam": 80,
        }        