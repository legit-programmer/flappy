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

    def draw(self):
        self.win.blit(self.sprite, (self.x, self.y))
        self.moveLeft()

    def checkCollision(self):
        bird = self.bird
        if bird.x + bird.width > self.x and bird.x < self.x+self.width:
            if bird.y < self.y+self.height and self.y < bird.y+bird.height:
                print('[FLAPPY CORE] Collision detected...')
                bird.vel = -bird.vel
                bird.vel_x = 5

    def moveLeft(self):
        self.x += self.x_vel


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
        pipe[0].checkCollision()
        pipe[1].checkCollision()
        
        # adding x_vel because its already a negative value
        if pipe[0].x == win.get_width()+pipe[0].x_vel:
            generatePipe(bird, pipes, win)

        if pipe[0].x < -600:  # delete pipes if it goes 600 pixel off the screen on x-axis

            pipes.pop(0)
            print(f'[FLAPPY CORE] Pipe instance at {hex(id(pipe))} deleted...')
