"""
@ Author: Robert Greenslade
@ Author: Anthony Ruffing
@ Author: Joshua Stanley
@
@ Title: Tower Defense Game - Tilemap
@
@ Date: June 20, 2022
"""

# Needed imports
import pygame
import constants
from constants import * 

# Texture and fill code
blue_surface = pygame.Surface((32,32))
blue_surface.fill(constants.BLUE_COLOR)
red_surface = pygame.Surface((32,32))
red_surface.fill(constants.RED_COLOR)

textures = {
    BLUE : blue_surface,
    RED : red_surface
}

# Full default tilemap
tilemap = [
    [RED, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, RED],
    [BLUE, RED, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, RED, BLUE],
    [BLUE, BLUE, RED, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, RED, BLUE, BLUE],
    [BLUE, BLUE, BLUE, RED, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, RED, BLUE, BLUE, BLUE],
    [BLUE, BLUE, BLUE, BLUE, RED, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, RED, BLUE, BLUE, BLUE, BLUE],
    [BLUE, BLUE, BLUE, BLUE, BLUE, RED, BLUE, BLUE, BLUE, BLUE, RED, BLUE, BLUE, BLUE, BLUE, BLUE],
    [BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, RED, BLUE, BLUE, RED, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE],
    [BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, RED, RED, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE],
    [BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, RED, RED, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE],
    [BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, RED, BLUE, BLUE, RED, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE],
    [BLUE, BLUE, BLUE, BLUE, BLUE, RED, BLUE, BLUE, BLUE, BLUE, RED, BLUE, BLUE, BLUE, BLUE, BLUE],
    [BLUE, BLUE, BLUE, BLUE, RED, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, RED, BLUE, BLUE, BLUE, BLUE],
    [BLUE, BLUE, BLUE, RED, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, RED, BLUE, BLUE, BLUE],
    [BLUE, BLUE, RED, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, RED, BLUE, BLUE],
    [BLUE, RED, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, RED, BLUE],
    [RED, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, RED],
]