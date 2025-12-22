class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((100, 100, 100)) # Grey walls
        self.rect = self.image.get_rect(topleft=(x, y))

# Setup
walls = pygame.sprite.Group()
walls.add(Wall(200, 200, 400, 20)) # A horizontal wall in the middle

# Inside your Game Loop update:
old_x, old_y = player.rect.topleft
player.update(keys)

# Check for collisions
if pygame.sprite.spritecollide(player, walls, False):
    player.rect.topleft = (old_x, old_y) # Reset position if hitting a wall