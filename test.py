import pygame

pygame.init()
screen = pygame.display.set_mode((640,640))

whalen = pygame.image.load('whalen.jpg')



running = True
x = 0 
clock = pygame.time.Clock()
while running: 
    
    screen.blit(whalen, (x, 30))
    x += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()