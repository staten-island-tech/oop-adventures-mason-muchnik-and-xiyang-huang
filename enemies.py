import pygame

class Skeleton(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.name = "Skeleton"
        try:
            self.image = pygame.image.load("skeleton.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (42, 42))
        except:
            self.image = pygame.Surface((40, 40))
            self.image.fill((200, 200, 200))
            
        self.rect = self.image.get_rect(topleft=(x, y))
        self.hitpoints = 10
        self.max_hp = 10
        self.attacks = {"Punch": 5, "Bone Throw": 10}

    def respawn(self):
        self.hitpoints = self.max_hp

class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.name = "Zombie"
        try:
            self.image = pygame.image.load("zombie.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (42, 42))
        except:
            self.image = pygame.Surface((40, 40))
            self.image.fill((100, 150, 100))
            
        self.rect = self.image.get_rect(topleft=(x, y))
        self.hitpoints = 30
        self.max_hp = 30
        self.attacks = {"Punch": 10, "Bite": 10}

    def respawn(self):
        self.hitpoints = self.max_hp