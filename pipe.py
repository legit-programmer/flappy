import pygame
import bird
import random


class Pipe:
    def __init__(self, bird: bird.Bird, win) -> None:
        self.sprite = pygame.image.load('assets/pipe2.png')
        self.height = self.sprite.get_height()
        self.width = self.sprite.get_width()
        self.x = 1280
        self.y = random.randrange(-700, -400)
        self.x_vel = -10
        self.bird = bird
        self.win = win
        self.y_offset = 300
        self.x_offset = 400
        self.passed = False

    def draw(self):
        self.win.blit(self.sprite, (self.x, self.y))
        self.moveLeft()

    def checkCollision(self):
        bird = self.bird
        if bird.x + bird.width > self.x and bird.x < self.x+self.width:
            if bird.y < self.y+self.height and self.y < bird.y+bird.height:
                print('[FLAPPY CORE] Collision detected...')
                bird.collided = True
                bird.resetPosition()
                return True
            
    def moveLeft(self):
        self.x += self.x_vel

def generateFirstPipe(bird, pipes:list, win):
    initP1 = Pipe(bird=bird, win=win)
    initP2 = Pipe(bird=bird, win=win)
    initP2.y = initP1.y + initP1.height + initP1.y_offset
    pipes.append((initP1, initP2))

def checkPass(bird:bird.Bird, pipes:list):
    for pipe in pipes:
        if not pipe[0].passed:
            if pipe[0].x + pipe[0].width< bird.x:
                pipe[0].passed = True
                bird.score+=1
                print(bird.score)

def generatePipe(bird: bird.Bird, pipes: list, win: pygame.Surface):
    pipe1 = Pipe(bird, win)
    pipe2 = Pipe(bird, win)
    pipe1.x = pipe2.x = win.get_width()+pipe1.x_offset
    pipe1.y = random.randrange(-700, -400)
    pipe2.y = pipe1.y + pipe1.height + pipe2.y_offset
    pipes.append((pipe1, pipe2))


def handlePipes(pipes: list, bird: bird.Bird, win: pygame.Surface):
    for pipe in pipes:
        pipe[0].draw()
        pipe[1].draw()


        # reseting pipe status
        if pipe[0].checkCollision() or pipe[1].checkCollision():
            pipes.clear()
            generateFirstPipe(bird, pipes, win)
            bird.collided = False
            bird.score = 0
            bird.isPlaying = False
            
        if not bird.collided:
            checkPass(bird, pipes)
        
        # adding x_vel because its already a negative value
        if pipe[0].x == win.get_width()+pipe[0].x_vel:
            generatePipe(bird, pipes, win)

        if pipe[0].x < -600:  # delete pipes if it goes 600 pixel off the screen on x-axis

            pipes.pop(0)
            print(f'[FLAPPY CORE] Pipe instance at {hex(id(pipe))} deleted...')
