# importing libraries
import random

import pygame

global event

# Initialising pygame
pygame.init()

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

font = pygame.font.SysFont("bahnschrift", 25)

# Window size
window_x, window_y = 800, 600
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('Pong')
fps = 60
overMessage = "GAME OVER!"

gameOver = False

paddleWidth = 10
paddleHieght = 90
paddleDist = 30

ballRadius = 10
ballCentre = [window_x//2, window_y//2]
player1 = pygame.Rect([paddleDist, window_y // 2 - paddleHieght // 2, paddleWidth, paddleHieght])
player2 = pygame.Rect([window_x - paddleDist, window_y // 2 - paddleHieght // 2, paddleWidth, paddleHieght])

player_speed = 5

move_p1 = 0
move_p2 = 0

move_ballX = 5
move_ballY = 0
# Speed is multiplied by this number
ballSpeedMulti = 1
# Adds this much to the ballSpeedMulti everytime the ball touches a paddle
ballSpeedMultiIncrease = 0.02
# a number between neg and pos this value is added to y ball movement
randomness = 1.5
# Max move_ballY
maxY = 4.5

def reset():
    global gameOver, ballCentre, move_p1, move_p2, move_ballX, move_ballY, ballSpeedMulti, ballSpeedMultiIncrease, player1, player2
    ballCentre = [window_x // 2, window_y // 2]

    player1 = pygame.Rect([paddleDist, window_y // 2 - paddleHieght // 2, paddleWidth, paddleHieght])
    player2 = pygame.Rect([window_x - paddleDist, window_y // 2 - paddleHieght // 2, paddleWidth, paddleHieght])

    move_p1 = 0
    move_p2 = 0
    move_ballX = 5
    move_ballY = 0
    ballSpeedMulti = 1
    gameOver = False


while True:
    while gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_SPACE:
                    reset()
        overMsg = font.render(overMessage, True, red)
        game_window.blit(overMsg,
                         [(window_x // 2) - (overMsg.get_width() // 2), (window_y // 2) - (overMsg.get_height() // 2)])
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key == pygame.K_w:
                move_p1 = -player_speed
            elif event.key == pygame.K_s:
                move_p1 = player_speed
            if event.key == pygame.K_UP:
                move_p2 = -player_speed
            elif event.key == pygame.K_DOWN:
                move_p2 = player_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                move_p1 = 0
            elif event.key == pygame.K_s:
                move_p1 = 0
            if event.key == pygame.K_UP:
                move_p2 = 0
            elif event.key == pygame.K_DOWN:
                move_p2 = 0

    player1.y = player1.y + move_p1
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= window_y:
        player1.bottom = window_y

    player2.y = player2.y + move_p2
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= window_y:
        player2.bottom = window_y

    ballCentre[0] = ballCentre[0] + move_ballX * ballSpeedMulti
    ballCentre[1] = ballCentre[1] + move_ballY
    ball_rect = pygame.Rect(ballCentre[0] - ballRadius, ballCentre[1] - ballRadius, ballRadius * 2, ballRadius * 2)

    if ball_rect.colliderect(player1) or ball_rect.colliderect(player2):
        move_ballX = -move_ballX
        ballSpeedMulti += ballSpeedMultiIncrease
        move_ballY = move_ballY + random.uniform(-randomness, randomness)
        if move_ballY > maxY:
            move_ballY = maxY
        elif move_ballY < -maxY:
            move_ballY = -maxY

    if ball_rect.top <= 0 or ball_rect.bottom >= window_y:
        move_ballY = -move_ballY

    if ball_rect.centerx < 0 or ball_rect.centerx > window_x:
        gameOver = True

    print(move_ballY)

    game_window.fill(black)
    pygame.draw.circle(game_window, red, ballCentre, ballRadius)
    pygame.draw.rect(game_window, blue, player1)
    pygame.draw.rect(game_window, green, player2)

    pygame.display.update()

    pygame.time.Clock().tick(fps)
