
import pygame
import bird
from pipe import Pipe, handlePipes, generateFirstPipe

# pygame setup
pygame.init()

WIDTH = 1280
HEIGHT = 720
ACCELERATION = 7
TIME_STEP = 0.3
FONT = pygame.font.Font('freesansbold.ttf', 32)
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
BACKGROUND = pygame.image.load('assets/bg.png')
flappyBird = bird.Bird(WIDTH, HEIGHT, ACCELERATION, TIME_STEP, win)
pipes = []


generateFirstPipe(bird=flappyBird, pipes=pipes, win=win)

x1, y1 = (0, 0)  # for background
x2, y2 = (1280, 0)


def showBackground():
    global x1, x2
    if x1+WIDTH <= 0:
        x1 = 1280
    elif x2+WIDTH <= 0:
        x2 = 1280
    win.blit(BACKGROUND, (x1, y1))
    win.blit(BACKGROUND, (x2, y2))
    x1 -= 1
    x2 -= 1


def drawScore():
    text = FONT.render(f'Score - {flappyBird.score}', True, (255, 255, 255))
    win.blit(text, (50, 50))


mx, my = (0, 0)

while running:

    showBackground()
    flappyBird.draw()
    drawScore()
    

    if flappyBird.isPlaying:
        handlePipes(pipes, flappyBird, win)
        flappyBird.applyGravity()
    else:
        pipes.clear()
        generateFirstPipe(flappyBird, pipes, win)
        win.blit(FONT.render('Press enter...', True,(255, 255, 255)), (flappyBird.x-75, flappyBird.y + 100))

    if flappyBird.follow:
        flappyBird.followDirection()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not flappyBird.collided:
                    flappyBird.fly()

            if event.key== pygame.K_RETURN:
                flappyBird.isPlaying = not flappyBird.isPlaying
                flappyBird.fly()
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     mx, my = pygame.mouse.get_pos()
        #     flappyBird.setupVector((mx, my))
        #     flappyBird.follow = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        flappyBird.y -= 5
    if keys[pygame.K_a]:
        flappyBird.x -= 5
    if keys[pygame.K_s]:
        flappyBird.y += 5
    if keys[pygame.K_d]:
        flappyBird.x += 5
    keys = pygame.key.get_pressed()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
