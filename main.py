import random
import math
import pygame

pygame.init()
font = pygame.font.SysFont("arial", 25)

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

# Scores
player1_score = 0
player2_score = 0

def reset():
    global ball_centre, ball_angle, ball_speed, game_over, player1, player2
    ball_centre = [screen.get_width() // 2, screen.get_height() // 2]
    ball_speed = 5
    ball_angle = random.choice([math.radians(random.randint(-45, 45)), math.radians(random.randint(135, 225))])
    player1.topleft = (paddle_dist, screen.get_height() // 2 - paddle_height // 2)
    player2.topleft = (screen.get_width() - paddle_dist, screen.get_height() // 2 - paddle_height // 2)
    return False


game_over = False
while True:
    if game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_over = reset()
        over_msg = font.render("Game Over", True, "red")
        screen.blit(over_msg, [(screen.get_width() // 2) - (over_msg.get_width() // 2), (screen.get_height() // 2) - (over_msg.get_height() // 2)])
        pygame.display.flip()
        continue

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

    # Scoring system
    if ball_rect.left <= 0:
        player2_score += 1
        game_over = True
    elif ball_rect.right >= screen.get_width():
        player1_score += 1
        game_over = True

    # Rendering
    screen.fill("black")
    pygame.draw.circle(screen, "red", ball_centre, ball_radius)
    pygame.draw.rect(screen, "blue", player1)
    pygame.draw.rect(screen, "green", player2)

    # Display scores
    score_text = font.render(f"{player1_score}  -  {player2_score}", True, "white")
    screen.blit(score_text, [(screen.get_width() // 2) - 20, 20])

    # Update Screen
    pygame.display.flip()
    clock.tick(fps)
