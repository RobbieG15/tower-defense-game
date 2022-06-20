import pygame
import constants

tilesize = 30
BLUE = 0
RED = 1

blue_surface = pygame.Surface((30,30))
blue_surface.fill(constants.BLUE)
red_surface = pygame.Surface((30,30))
red_surface.fill(constants.RED)


textures = {
    BLUE : blue_surface,
    RED : red_surface
}

tilemap = [
    [BLUE, BLUE, BLUE, BLUE],
    [BLUE, BLUE, RED, BLUE],

]