import pygame
import bird
import random
class Pipe:
    def __init__(self, bird:bird.Bird, win) -> None:
        self.sprite = pygame.image.load('assets/pipe2.png')
        self.height = self.sprite.get_height()
        self.width = self.sprite.get_width()
        self.x = 1280
        self.y = -500
        self.x_vel = -2
        self.bird = bird
        self.win = win
        self.offset = 300

    def draw(self):
        self.win.blit(self.sprite, (self.x, self.y))
        self.moveLeft()

    def checkCollision(self):
        bird = self.bird
        if bird.x + bird.width>self.x and bird.x<self.x+self.width:
            if bird.y < self.y+self.height and self.y<bird.y+bird.height:
                print('collided')
                bird.collided = True

    def moveLeft(self):
        self.x+=self.x_vel

def generatePipe(bird:bird.Bird, pipes:list, win):
    pipe1 = Pipe(bird, win)
    pipe2 = Pipe(bird, win)
    pipe1.x = 1280+200
    pipe1.y = random.randrange(-700, -400)
    pipe2.x = 1280+200
    pipe2.y = pipe1.y + 720 + pipe2.offset
    pipes.append((pipe1, pipe2))

def handlePipes(pipes:list, bird:bird.Bird, win):
    for pipe in pipes:
        pipe[0].draw()
        pipe[1].draw()
        pipe[0].checkCollision()
        pipe[1].checkCollision()
        if pipe[0].x == 1278:
            print('sdfdsf')
            generatePipe(bird, pipes, win)
        
        if pipe[0].x<-500:
            pipes.pop(0)
            print('pipe deleted')