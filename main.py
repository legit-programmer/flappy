
import pygame
import bird
from pipe import Pipe

# pygame setup
pygame.init()
WIDTH = 1280
HEIGHT = 720
ACCELERATION = 5
TIME_STEP = 0.3
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True


            
            

flappyBird = bird.Bird(WIDTH, HEIGHT, ACCELERATION, TIME_STEP, win)
pipe = Pipe(bird=flappyBird, win=win)

while running:
    
    win.fill("white")
    flappyBird.draw()
    pipe.draw()

    flappyBird.applyGravity()
    flappyBird.checkCollision()
    pipe.checkCollision()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flappyBird.fly()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        flappyBird.y-=5
    if keys[pygame.K_a]:
        flappyBird.x-=5
    if keys[pygame.K_s]:
        flappyBird.y+=5
    if keys[pygame.K_d]:
        flappyBird.x+=5
    keys = pygame.key.get_pressed()
        
    pygame.display.flip()

    clock.tick(60)  

pygame.quit()
