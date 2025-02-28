import pygame

pygame.init()

# Window setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()
fps = 60

while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Rendering
    screen.fill("black")

    # Update Screen
    pygame.display.flip()
    clock.tick(fps)
