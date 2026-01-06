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

class Troll():
    def __init__(self):
        self.hitpoints = 200
        self.speed = 160
        self.xp = 40
        self.attacks = {
            "Slam": 50,
        }

class ElderTroll():
    def __init__(self):
        self.hitpoints = 300
        self.speed = 180
        self.xp = 60
        self.attacks = {
            "Slam": 80,
        }