import pygame
from pygame.locals import *
from person import Human
from config import *

# Init Pygame
pygame.init()
clock = pygame.time.Clock()


# Create screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# create group of human
all_human = pygame.sprite.Group()
for i in range(AMOUNT_HUMANS):
    if i == 1:
        human = Human(is_infected=True)
    else:
        human = Human()
    all_human.add(human)


# Variable tu keep game loop running
running = True

# Game Loop
while running:

    #---------EVENTS---------------------------------
    # Get every event
    for event in pygame.event.get():
        # Check if user hit a key
        if event.type == KEYDOWN:
            # Check if it was ESC
            if event.key == K_ESCAPE:
                running = False

        # Check if user clicked close
        if event.type == pygame.QUIT:
            running = False

    #Randomly move humans
    for human in all_human:
        human.move()
        human.check_collision(all_human)


    # --------DISPLAY----------------------------------
    # Fill Screen Black
    screen.fill(BLACK)

    # Draw entities
    for human in all_human:
        screen.blit(human.surf, human.rect)

    # Update display
    pygame.display.flip()

    #Sets framerate
    clock.tick(30)