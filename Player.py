import pygame
import random
from WeaponsArmor import Weapons

class Player(pygame.sprite.Sprite):
    def __init__(self, race, x, y):
        super().__init__()
        self.race = race
        
        # Try to load image, fallback to square
        try:
            self.image = pygame.image.load("human.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (42, 42))
        except:
            self.image = pygame.Surface((40, 40))
            self.image.fill((0, 200, 0))
            
        self.rect = self.image.get_rect(topleft=(x, y))
        self.inventory = []
        
        # Stats based on your framework
        if race in ("Human", "human", "1"):
            self.hitpoints = 100
            self.max_hp = 100
            self.speed = 4
            self.inventory.append("Starter Sword")
        elif race in ("Goblin", "goblin", "2"):
            self.hitpoints = 80
            self.max_hp = 80
            self.speed = 6
            self.inventory.append("Starter Dagger")
        elif race in ("Ogre", "ogre", "3"):
            self.hitpoints = 120
            self.max_hp = 120
            self.speed = 2
            self.inventory.append("Starter Club")

    def move(self, dx, dy, walls):
        # Move horizontally
        if dx != 0:
            self.rect.x += dx * self.speed
            # Check for wall collisions
            if pygame.sprite.spritecollideany(self, walls):
                self.rect.x -= dx * self.speed

        # Move vertically
        if dy != 0:
            self.rect.y += dy * self.speed
            # Check for wall collisions
            if pygame.sprite.spritecollideany(self, walls):
                self.rect.y -= dy * self.speed

    def take_damage(self, enemy):
        attack = random.choice(list(enemy.attacks.keys()))
        damage = enemy.attacks[attack]
        self.hitpoints = max(0, self.hitpoints - damage)
        return damage
    
    def attack(self, enemy):
        for item in self.inventory:
            for weapon in Weapons:
                if weapon["name"] == item:
                    damage = weapon["damage"]
                    enemy.hitpoints = max(0, enemy.hitpoints - damage)
                    return damage