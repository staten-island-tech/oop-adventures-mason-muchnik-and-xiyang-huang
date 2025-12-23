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

test = ElderTroll()
print(test.hitpoints)