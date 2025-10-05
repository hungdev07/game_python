import pygame
from time import sleep
from random import randint

pygame.init()
screen = pygame.display.set_mode((601, 601))
pygame.display.set_caption('Snake')
running = True
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
clock = pygame.time.Clock()

# tail - head
snakes = [[5, 10]]
direction = "right"

apple = [randint(0, 19), randint(0, 19)]
font_small = pygame.font.SysFont('sans', 20)
font_big = pygame.font.SysFont('sans', 50)
score = 0
pausing = False

while running:
    clock.tick(60)
    screen.fill(BLACK)
    tail = snakes[0]

    #Draw grid
    for i in range(21):
        pygame.draw.line(screen, WHITE, (0, i * 30), (600, i * 30))
        pygame.draw.line(screen, WHITE, (i * 30, 0), (i * 30, 600))
    
    #Draw snake
    for snake in snakes:
        pygame.draw.rect(screen, GREEN, (snake[0] * 30, snake[1] * 30, 30, 30))
    
    #Draw apple
    pygame.draw.rect(screen, RED, (apple[0] * 30, apple[1] * 30, 30, 30))
    
    if snakes[-1][0] == apple[0] and snakes[-1][1] == apple[1]:
        snakes.insert(0, [tail[0], tail[1]])
        apple = [randint(0, 19), randint(0, 19)]
        score += 1
        while apple in snakes:
            apple = [randint(0, 19), randint(0, 19)]
    
    #check crash
    
    snakes_tmp = snakes[0: len(snakes) - 2]

    if snakes[-1][0] < 0 or snakes[-1][0] > 19 or snakes[-1][1] < 0 or snakes[-1][1] > 19 or snakes[-1] in snakes_tmp:
        game_over_txt = font_big.render("Game over, score: " + str(score), True, WHITE)
        screen.blit(game_over_txt, (50, 200))
        press_space_txt = font_big.render("Press space to continue", True, WHITE)
        screen.blit(press_space_txt, (50, 300))
        pausing = True
    
    #draw score
    score_txt = font_small.render(f"Score: {score}", True, WHITE)
    screen.blit(score_txt, (0, 0))

    #snake move
    if pausing == False: 
        if direction == "right":
            snakes.append([snakes[-1][0] + 1, snakes[-1][1]])
            snakes = snakes[1:]
        if direction == "left":
            snakes.append([snakes[-1][0] - 1, snakes[-1][1]])
            snakes = snakes[1:]
        if direction == "up":
            snakes.append([snakes[-1][0], snakes[-1][1] - 1])
            snakes = snakes[1:]
        if direction == "down":
            snakes.append([snakes[-1][0], snakes[-1][1] + 1])
            snakes = snakes[1:]
    
    sleep(0.05)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                direction = "up"
            elif event.key == pygame.K_DOWN and direction != "up":
                direction = "down"
            elif event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            elif event.key == pygame.K_RIGHT and direction != "left": 
                direction = "right"
            if event.key == pygame.K_SPACE and pausing == True:
                pausing = False
                snakes = [[5, 10]]
                apple = [randint(0, 19), randint(0, 19)]
                score = 0
    pygame.display.flip()

pygame.quit()