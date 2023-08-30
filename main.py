
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
        self.sprite = pygame.image.load('assets/bird.png')
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
        
            
    
    def checkCollision(self):
        if not self.y+self.height<=HEIGHT:
            self.vel = -(self.vel)
        
        
    def draw(self):
        # self.rect.top = self.y
        # self.rect.left = self.x
        win.blit(self.sprite, (self.x, self.y))

    def fly(self):
    
        self.vel = -(self.vel + 150) * TIME_STEP
        
        # self.y -= 20

        

flappyBird = Bird()

while running:
    
    win.fill("white")
    flappyBird.draw()

    if not flappyBird.flying:
        flappyBird.applyGravity()
        flappyBird.checkCollision()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         flappyBird.fly()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        flappyBird.fly()
    keys = pygame.key.get_pressed()
    
    
    

    
    pygame.display.flip()

    clock.tick(60)  

pygame.quit()
