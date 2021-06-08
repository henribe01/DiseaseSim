import random

import pygame

from config import *


class Human(pygame.sprite.Sprite):
    def __init__(self, is_infected=False):
        super(Human, self).__init__()
        self.width, self.height = 5, 5
        self.surf = pygame.Surface((self.width, self.height))
        self.vel_x = 0
        self.vel_y = 0
        self.radius = self.width / 2
        self.is_infected = is_infected

        self.surf.set_colorkey(BLACK)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
        self.surf.fill(BLACK)
        pygame.draw.circle(self.surf, WHITE, (self.width / 2, self.height / 2), self.radius)
        if self.is_infected:
            self.infect()

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

        # Teleport to other side with rect is crossing border
        if self.rect.left < 0:
            self.rect.left = SCREEN_WIDTH - self.width
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = 0 + self.width
        if self.rect.top < 0:
            self.rect.top = SCREEN_HEIGHT - self.height
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = 0 + self.height

    def check_collision(self, group):
        hits = pygame.sprite.spritecollide(self, group, False)
        if len(hits) >= 2:
            self.vel_x = 0
            self.vel_y = 0

            for human in hits:
                if human.is_infected:
                    self.infect()

    def infect(self):
        self.is_infected = True
        pygame.draw.circle(self.surf, RED, (self.width / 2, self.height / 2), self.radius)
