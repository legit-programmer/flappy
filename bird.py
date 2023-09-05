import pygame

class Bird:
    def __init__(self, WIDTH, HEIGHT, ACCELERATION, TIME_STEP, win) -> None:
        self.sprite = pygame.transform.scale(pygame.image.load('assets/bird.png'), (32, 32))
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.WIN_WIDTH = WIDTH
        self.WIN_HEIGHT = HEIGHT
        self.x = WIDTH/2-self.width/2
        self.y = HEIGHT/2-self.height/2
        self.vel = 5
        self.ACCELERATION = ACCELERATION
        self.TIME_STEP = TIME_STEP
        self.win = win
        self.collided = False
        self.vel_x = 0
        

    def applyGravity(self):
        if not self.collided:
            self.vel+= self.ACCELERATION * self.TIME_STEP
            self.y += self.vel * self.TIME_STEP
            self.x -=self.vel_x
    def resetPosition(self):
        self.x = self.WIN_WIDTH/2-self.width/2
        self.y = self.WIN_HEIGHT/2-self.height/2

    def checkCollision(self):
        if not self.y+self.height<=self.WIN_HEIGHT:
            self.vel = -(self.vel)
            self.collided = True
            self.y = self.WIN_HEIGHT-self.height
            self.vel_x = 0
        
    def draw(self):
        self.win.blit(self.sprite, (self.x, self.y))

    def fly(self):
        self.vel = -(self.vel + 100) * self.TIME_STEP