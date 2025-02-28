import random
import math
import pygame

pygame.init()

# Window setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()
fps = 60

# Ball settings
ball_speed = 5
ball_angle = random.choice([math.radians(random.randint(-45, 45)), math.radians(random.randint(135, 225))])
ball_radius = 10
ball_centre = [screen.get_width() // 2, screen.get_height() // 2]
ball_speed_increment = 0.2

# Paddle settings
paddle_width = 10
paddle_height = 90
paddle_dist = 30

# Player settings
player_speed = 5
player1 = pygame.Rect(paddle_dist, screen.get_height() // 2 - paddle_height // 2, paddle_width, paddle_height)
player2 = pygame.Rect(screen.get_width() - paddle_dist - paddle_width, screen.get_height() // 2 - paddle_height // 2, paddle_width, paddle_height)

while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Player controls
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_w]:
        player1.y -= player_speed
    if pressed_keys[pygame.K_s]:
        player1.y += player_speed
    if pressed_keys[pygame.K_UP]:
        player2.y -= player_speed
    if pressed_keys[pygame.K_DOWN]:
        player2.y += player_speed

    # Keep paddles within screen bounds
    for player in [player1, player2]:
        if player.top < 0:
            player.top = 0
        if player.bottom > screen.get_height():
            player.bottom = screen.get_height()

    # Ball movement
    ball_centre[0] = ball_centre[0] + math.cos(ball_angle) * ball_speed
    ball_centre[1] = ball_centre[1] + math.sin(ball_angle) * ball_speed

    ball_rect = pygame.Rect(ball_centre[0] - ball_radius, ball_centre[1] - ball_radius, ball_radius * 2, ball_radius * 2)

    # Ball collision with paddles
    if ((ball_rect.colliderect(player1) and math.cos(ball_angle) < 0)
            or (ball_rect.colliderect(player2) and math.cos(ball_angle) > 0)):
        ball_angle = math.pi - ball_angle
        ball_speed += ball_speed_increment

    # Ball collision with top/bottom walls
    if ball_rect.top <= 0 or ball_rect.bottom >= screen.get_height():
        ball_angle = math.pi * 2 - ball_angle

    # Rendering
    screen.fill("black")
    pygame.draw.circle(screen, "red", ball_centre, ball_radius)
    pygame.draw.rect(screen, "blue", player1)
    pygame.draw.rect(screen, "green", player2)

    # Update Screen
    pygame.display.flip()
    clock.tick(fps)
