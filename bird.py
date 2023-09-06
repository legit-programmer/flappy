import pygame
import math
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
        self.follow = False
        self.pos:tuple
        self.originX:int
        self.originY:int
        

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

    def setupVector(self, pos):
        mouse_x, mouse_y = self.pos = pos 
        self.originX, self.originY = self.x, self.y
        dx = self.x - mouse_x
        dy = self.y - mouse_y
        d = math.sqrt(dx**2 + dy**2)
        self.ux = dx/d
        self.uy = dy/d
        

    def followDirection(self): # utility funtion
        
        #pos[0] = mouseX pos[1] = mouseY
        if not (math.floor(self.x) in range(self.pos[0]-10, self.pos[0]+10) and math.floor(self.y) in range(self.pos[1]-10, self.pos[1]+10)):
            pygame.draw.line(self.win, (0, 0, 0), (self.originX, self.originY), (self.pos[0], self.pos[1]), 3)
            pygame.draw.line(self.win, (0, 0, 0), (self.originX, self.originY), (self.pos[0], self.originY), 3)
            pygame.draw.line(self.win, (0, 0, 0), (self.pos[0], self.originY), (self.pos[0], self.pos[1]), 3)
            self.x-=self.ux * 5
            self.y-=self.uy * 5
        
        else:
            self.follow = False
        
        print('[FLAPPY CORE]Following...')

    
        