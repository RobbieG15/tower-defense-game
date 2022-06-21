"""
@ Author: Robert Greenslade
@ Author: Anthony Ruffing 
@ Author: Joshua Stanley 
@
@ Title: Tower Defense Game
@
@ Date: June 28, 2021
"""

# Imports Needed
import pygame
import random
import tilemap
from constants import *

# Initializing Pygame and Window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense Game")
clock = pygame.time.Clock()

# Player
speed = 3
player_x, player_y = 20, 20
player = pygame.Rect((player_x,player_y),(10,10))

def ProcessInput():
    global running

    # Process input (events)
    for event in pygame.event.get():
        
        # Check for closing window
        if event.type == pygame.QUIT:
            running = False
        # Mouse click
        elif event.type == pygame.MOUSEBUTTONUP:
            # Use floor division to get the indices of the tile.
            x = event.pos[0] // TILESIZE
            y = event.pos[1] // TILESIZE

            no_list = [[14,15,16],[10,11,12]]
            if x not in no_list[0] or y not in no_list[1]: 
                if event.button == 1: # Left mouse button 
                    tilemap.tilemap[y][x] = RED
                if event.button == 3: # Right mouse button 
                    tilemap.tilemap[y][x] = BLUE 
   
    # Checking key pressed
    keys = pygame.key.get_pressed() 
    
    if keys[pygame.K_a]:
        player.x -= speed
    if keys[pygame.K_d]:
        player.x += speed
    if keys[pygame.K_s]:
        player.y += speed
    if keys[pygame.K_w]:
        player.y -= speed

# Main Game Loop
running = True
while running:
    ProcessInput()
    
    # Update
    pygame.display.update()
    clock.tick(FPS)

    # Draw / Render
    screen.fill(BLACK_COLOR)
    
    # Tilemap drawing every frame
    for row in range( len(tilemap.tilemap) ):
        for column in range( len(tilemap.tilemap[row]) ):
            screen.blit(tilemap.textures[tilemap.tilemap[row][column]],
                    (column*TILESIZE, row*TILESIZE))

    pygame.draw.rect(screen,RED_COLOR,player)