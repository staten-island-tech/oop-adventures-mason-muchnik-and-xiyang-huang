class Skeleton():
    def __init__(self, hitpoints, speed, xp, attacks):
        self.hitpoints = hitpoints
        self.speed = speed
        self.xp = xp
        self.attacks = attacks

        hitpoints = 10
        speed = 180
        xp = 5
        attacks = {
            "Punch": 5,
            "Bone Throw": 10
        }

class Zombie():
    def __init__(self, hitpoints, speed, xp, attacks):
        self.hitpoints = hitpoints
        self.speed = speed
        self.xp = xp
        self.attacks = attacks

        hitpoints = 30
        speed = 160
        xp = 5
        attacks = {
            "Punch": 10,
            "Bite": 10
        }

class Wolves():
    def __init__(self, hitpoints, speed, xp, attacks):
        self.hitpoints = hitpoints
        self.speed = speed
        self.xp = xp
        self.attacks = attacks

        hitpoints = 25
        speed = 300
        xp = 10
        attacks = {
            "Bite": 15,
        }

class BabyTroll():
    def __init__(self, hitpoints, speed, xp, attacks):
        self.hitpoints = hitpoints
        self.speed = speed
        self.xp = xp
        self.attacks = attacks

        hitpoints = 50
        speed = 160
        xp = 20
        attacks = {
            "Punch": 30,
        }