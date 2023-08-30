
import pygame

# pygame setup
pygame.init()
WIDTH = 1280
HEIGHT = 720
ACCELERATION = 5
TIME_STEP = 0.3
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True




class Bird:
    def __init__(self) -> None:
        self.sprite = pygame.transform.scale(pygame.image.load('assets/bird.png'), (32, 32))
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.x = WIDTH/2-self.width/2
        self.y = HEIGHT/2-self.height/2
        self.vel = 5
        self.flying = False
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((255, 255, 0))
        self.angle = 3
        self.rect = self.surface.get_rect()

    def applyGravity(self):
        self.vel+=ACCELERATION * TIME_STEP
        self.y += self.vel * TIME_STEP
    
    def resetPosition(self):
        self.x = WIDTH/2-self.width/2
        self.y = HEIGHT/2-self.height/2

    def checkCollision(self):
        if not self.y+self.height<=HEIGHT:
            self.vel = -(self.vel*0.5)
            self.resetPosition()
        
        
    def draw(self):
        win.blit(self.sprite, (self.x, self.y))

    def fly(self):
        self.vel = -(self.vel + 100) * TIME_STEP


class Pipe:
    def __init__(self, bird:Bird) -> None:
        self.sprite = pygame.image.load('assets/pipe.png')
        self.height = self.sprite.get_height()
        self.width = self.sprite.get_width()
        self.x = 0
        self.y = 500
        self.x_vel = -2
        self.bird = bird

    def draw(self):
        win.blit(self.sprite, (self.x, self.y))

    def checkCollision(self):
        bird = self.bird
        if bird.x + bird.width>self.x and bird.x<self.x+self.width:
            if bird.y < self.y+self.height and self.y<bird.y+bird.height:
                print('collided')
            # if bird.x<
            

flappyBird = Bird()
pipe = Pipe(bird=flappyBird)

while running:
    
    win.fill("white")
    flappyBird.draw()
    pipe.draw()

    if not flappyBird.flying:
        # flappyBird.applyGravity()
        # flappyBird.checkCollision()
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
