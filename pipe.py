import pygame
import bird

class Pipe:
    def __init__(self, bird:bird.Bird, win) -> None:
        self.sprite = pygame.image.load('assets/pipe2.png')
        self.height = self.sprite.get_height()
        self.width = self.sprite.get_width()
        self.x = 650
        self.y = 500
        self.x_vel = -2
        self.bird = bird
        self.win = win

    def draw(self):
        self.win.blit(self.sprite, (self.x, self.y))

    def checkCollision(self):
        bird = self.bird
        if bird.x + bird.width>self.x and bird.x<self.x+self.width:
            if bird.y < self.y+self.height and self.y<bird.y+bird.height:
                print('collided')
                bird.collided = True