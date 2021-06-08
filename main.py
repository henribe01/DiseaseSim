import pygame
from pygame.locals import *
from person import Human
from config import *

# Init Pygame
pygame.init()
clock = pygame.time.Clock()


# Create screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))

# Create Human
human = Human()

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

    #Randomly move human
    human.move()

    # --------DISPLAY----------------------------------
    # Fill Screen Black
    screen.fill(BLACK)

    # Draw human
    screen.blit(human.surf, human.rect)

    # Update display
    pygame.display.flip()

    #Sets framerate
    clock.tick(30)