class Enemy:
    def __init__(self, name, hp, speed, xp, attacks):
        self.name = name
        self.maxhp = hp
        self.hitpoints = hp
        self.speed = speed
        self.xp = xp
        self.attacks = attacks

    def respawn(self):
        self.hitpoints = self.maxhp


Skeleton = Enemy(
    "Skeleton", 10, 180, 20,
    {"Punch": 5, "Bone Throw": 10}
)

Zombie = Enemy(
    "Zombie", 30, 160, 20,
    {"Punch": 10, "Bite": 10}
)

Wolf = Enemy(
    "Wolf", 25, 300, 20,
    {"Bite": 15}
)

BabyTroll = Enemy(
    "Baby Troll", 50, 160, 60,
    {"Punch": 30}
)

Troll = Enemy(
    "Troll", 150, 160, 80,
    {"Slam": 50}
)

ElderTroll = Enemy(
    "Elder Troll", 300, 180, 100,
    {"Slam": 80}
)
DemonLord = Enemy(
    "Demon Lord", 500, 220, 150,
    {"Hell Slash": 70, "Inferno": 120}
)

VoidReaper = Enemy(
    "Void Reaper", 650, 240, 200,
    {"Void Cleave": 90, "Soul Rip": 140}
)

AncientDragon = Enemy(
    "Ancient Dragon", 900, 200, 300,
    {"Fire Breath": 160, "Tail Smash": 120, "Claw Rend": 100}
)

ElderLich = Enemy(
    "Elder Lich", 550, 260, 250,
    {"Death Bolt": 110, "Life Drain": 140}
)

TitanOfOblivion = Enemy(
    "Titan of Oblivion", 1200, 180, 400,
    {"World Crusher": 200, "Seismic Slam": 160}
)

starterenemies = [Skeleton, Zombie, Wolf]
midenemies = [BabyTroll, Troll, ElderTroll]
endenemies = [DemonLord, VoidReaper, AncientDragon, ElderLich, TitanOfOblivion]
