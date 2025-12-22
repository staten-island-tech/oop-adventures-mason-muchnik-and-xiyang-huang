import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, race="Human"):
        super().__init__()
        
        # --- PARTNER'S SECTION: STATS & DATA ---
        self.race = race
        self.level = 1
        self.hp = 100
        self.max_hp = 100
        self.strength = 10
        self.inventory = []
        self.equipment = {"Head": None, "Chest": None, "Weapon": None}
        
        # --- YOUR SECTION: VISUALS & PHYSICS ---
        # Note: You will replace these placeholders with actual images later
        self.image = pygame.Surface((32, 48)) 
        self.image.fill((0, 255, 0)) # Placeholder color
        self.rect = self.image.get_rect(topleft=(x, y))
        
        self.speed = 4
        self.direction = "down" # Useful for knowing which way to face
        self.is_moving = False

    def update(self, keys):
        """Handle movement logic"""
        self.is_moving = False
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.direction = "left"
            self.is_moving = True
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
            self.direction = "right"
            self.is_moving = True
            
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.direction = "up"
            self.is_moving = True
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
            self.direction = "down"
            self.is_moving = True

    def take_damage(self, amount):
        """A sample backend function your partner might write"""
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0




#race LOGIC


# Example of how you'd load images based on race
if player.race == "Elf":
    player.image = pygame.image.load("assets/sprites/elf_idle.png")
elif player.race == "Orc":
    player.image = pygame.image.load("assets/sprites/orc_idle.png")