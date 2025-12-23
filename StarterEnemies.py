class Skeleton():
    def __init__(self):
        self.hitpoints = 10
        self.speed = 180
        self.xp = 5
        self.attacks = {
            "Punch": 5,
            "Bone Throw": 10
        }

class Zombie():
    def __init__(self):
        self.hitpoints = 30
        self.speed = 160
        self.xp = 5
        self.attacks = {
            "Punch": 10,
            "Bite": 10
        }

class Wolves():
    def __init__(self):
        self.hitpoints = 25
        self.speed = 300
        self.xp = 10
        self.attacks = {
            "Bite": 15,
        }

class BabyTroll():
    def __init__(self):
        self.hitpoints = 50
        self.speed = 160
        self.xp = 20
        self.attacks = {
            "Punch": 30,
        }

test = BabyTroll()
print(test.xp)