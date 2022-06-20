"""
@ Author: Robert Greenslade
@ Author: Anthony Ruffing
@ Author: Joshua Stanley
@
@ Title: Pygame Template 
@
@ Date: June 28, 2021
"""

# Imports Needed
import pygame
import random

# Constant Variables
WIDTH = 640
HEIGHT = 360
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initializing Pygame and Window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense Game")
clock = pygame.time.Clock()
player = pygame.Rect((20,20),(10,10))

# Main Game Loop
running = True
while running:

    # Process input (events)
    for event in pygame.event.get():
        
        # Check for closing window
        if event.type == pygame.QUIT:
            running = False

        # Checking key presses
        keys = pygame.key.get_pressed()
    
    # Update
    pygame.display.update()
    clock.tick(FPS)

    # Draw / Render
    screen.fill(BLACK)
    pygame.draw.rect(screen,RED,player)