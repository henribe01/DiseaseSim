import pygame
import random
from config import *

class Human(pygame.sprite.Sprite):
    def __init__(self):
        super(Human, self).__init__()
        self.width, self.height = 10, 10
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill(BLACK)
        pygame.draw.circle(self.surf, WHITE, (self.width/2, self.height/2), self.width/2)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
        self.vel_x = 0
        self.vel_y = 0

    def move(self):
        self.vel_x = self.vel_x + random.randint(-SPEED, SPEED)
        self.vel_y = self.vel_y + random.randint(-SPEED, SPEED)
        if self.vel_x > MAX_SPEED:
            self.vel_x = MAX_SPEED
        elif self.vel_x < -MAX_SPEED:
            self.vel_x = -MAX_SPEED
        if self.vel_y > MAX_SPEED:
            self.vel_y = MAX_SPEED
        elif self.vel_y < -MAX_SPEED:
            self.vel_y = -MAX_SPEED
        self.rect.move_ip(self.vel_x, self.vel_y)
        print(self.vel_x, self.vel_y)

        #Borders
        if self.rect.left < 0:
            self.rect.left = SCREEN_WIDTH - self.width
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = 0 + self.width
        if self.rect.top < 0:
            self.rect.top = SCREEN_HEIGHT - self.height
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = 0 + self.height