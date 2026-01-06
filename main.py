import pygame
import sys
from Player import Player
from enemies import Skeleton, Zombie

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)

TILE_SIZE = 40
# Map layout: 1 is Wall, 0 is Floor
COMPLEX_MAP = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1],
    [1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1],
    [1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1],
    [1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill((50, 50, 50))
        self.rect = self.image.get_rect(topleft=(x, y))

# Setup Groups
all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Build Map
for r, row in enumerate(COMPLEX_MAP):
    for c, tile in enumerate(row):
        if tile == 1:
            w = Wall(c*TILE_SIZE, r*TILE_SIZE)
            walls.add(w)
            all_sprites.add(w)

player = Player("Human", 50, 50)
zombie = Zombie(400, 280)
all_sprites.add(player, zombie)
enemies.add(zombie)

while True:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        
        # Attack with Space
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            hit = pygame.sprite.spritecollideany(player, enemies)
            if hit:
                player.attack(hit)
                if hit.hitpoints > 0: player.take_damage(hit)
                else: hit.respawn()

    # MOVEMENT FIX: Simplified key detection
    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_LEFT]:  dx = -1
    if keys[pygame.K_RIGHT]: dx = 1
    if keys[pygame.K_UP]:    dy = -1
    if keys[pygame.K_DOWN]:  dy = 1
    
    player.move(dx, dy, walls)

    all_sprites.draw(screen)
    
    # UI Health Bars
    pygame.draw.rect(screen, (255,0,0), (player.rect.x, player.rect.y-10, 40, 5))
    pygame.draw.rect(screen, (0,255,0), (player.rect.x, player.rect.y-10, 40*(player.hitpoints/player.max_hp), 5))
    
    pygame.display.flip()
    clock.tick(60)