import pygame

# --- INITIALIZATION ---
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# --- UTILITY FUNCTIONS ---
def get_image(sheet, frame, width, height, scale):
    """Cuts an image out of a sprite sheet"""
    image = pygame.Surface((width, height)).convert_alpha()
    # (source_surface, destination, area_on_source)
    image.blit(sheet, (0, 0), (frame * width, 0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey((0, 0, 0)) # Makes black background transparent
    return image

# --- CLASSES ---
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # 1. Load Sprite Sheet (Replace 'player_sheet.png' with your file)
        # For now, we create a placeholder surface if you don't have the file yet
        self.sprites = []
        for i in range(4): # Assume 4 frames of animation
            temp_surf = pygame.Surface((32, 32))
            temp_surf.fill((50, 150, 255) if i % 2 == 0 else (100, 200, 255))
            self.sprites.append(temp_surf)
        
        self.current_frame = 0
        self.image = self.sprites[self.current_frame]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 4
        self.is_moving = False

    def update(self, keys):
        self.is_moving = False
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.is_moving = True
        if keys[pygame.K_d]:
            self.rect.x += self.speed
            self.is_moving = True
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.is_moving = True
        if keys[pygame.K_s]:
            self.rect.y += self.speed
            self.is_moving = True

        # 2. Simple Animation Logic
        if self.is_moving:
            self.current_frame += 0.1 # Adjust speed of animation
            if self.current_frame >= len(self.sprites):
                self.current_frame = 0
            self.image = self.sprites[int(self.current_frame)]

class GUI:
    @staticmethod
    def draw_health_bar(screen, x, y, hp, max_hp):
        ratio = hp / max_hp
        pygame.draw.rect(screen, (255, 0, 0), (x, y, 200, 20)) # Red back
        pygame.draw.rect(screen, (0, 255, 0), (x, y, 200 * ratio, 20)) # Green front

# --- GAME SETUP ---
player = Player(400, 300)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Placeholder for Map
# background = pygame.image.load("map.png").convert()

# --- MAIN LOOP ---
running = True
player_hp = 80 # This logic will eventually come from your partner's code

while running:
    screen.fill((30, 30, 30)) # Clear Screen
    
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Logic / Update
    keys = pygame.key.get_pressed()
    all_sprites.update(keys)

    # 3. Drawing
    # screen.blit(background, (0,0)) # Draw map first
    all_sprites.draw(screen) # Draw characters
    
    # Draw GUI last (on top)
    GUI.draw_health_bar(screen, 20, 20, player_hp, 100)
    img_text = font.render(f"Health: {player_hp}/100", True, (255, 255, 255))
    screen.blit(img_text, (20, 45))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()