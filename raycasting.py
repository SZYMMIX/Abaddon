import pygame
import math
from settings import *

class RayCasting:
    def __init__(self, game):
        self.game = game

    def update(self):
        self.ray_cast()

    def ray_cast(self):
        ox, oy = self.game.player.x, self.game.player.y
        ray_angle = self.game.player.angle - HALF_FOV
        

        for ray in range(NUM_RAYS):

            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)
            x, y = ox, oy 

            for depth in range(int(MAX_DEPTH * 100)): 
                x += 0.01 * cos_a
                y += 0.01 * sin_a

                if (int(x), int(y)) in self.game.map.world_map:
                    dist = depth * 0.01
                    dist *= math.cos(self.game.player.angle - ray_angle)
                    proj_height = SCREEN_DIST / (dist + 0.0001)

                    c = 255 / (1 + dist * 0.4) 
                    c = int(c)
                    color = (c, c, c)

                    pygame.draw.rect(self.game.display, color,
                                    (ray * SCALE, HEIGHT // 2 - proj_height // 2, 
                                     SCALE, proj_height))

                    break 
            ray_angle += DELTA_ANGLE