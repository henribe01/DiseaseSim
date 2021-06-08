import pygame
import random
from config import *

class Human(pygame.sprite.Sprite):
    def __init__(self):
        super(Human, self).__init__()
        self.width, self.height = 10, 10
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill((0,0,0))
        pygame.draw.circle(self.surf, (255,255,255), (self.width/2, self.height/2), self.width/2)
        self.rect = self.surf.get_rect()

    def move(self):
        direction_list = ['N', 'E', 'S', 'W']
        direction = random.choice(direction_list)
        if direction == 'N':
            self.rect.move_ip(0, -10)
        elif direction == 'E':
            self.rect.move_ip(10, 0)
        elif direction == 'S':
            self.rect.move_ip(0, 10)
        elif direction == 'W':
            self.rect.move_ip(-10, 0)

        #Borders
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT