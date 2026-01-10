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
        

        for _ in range(NUM_RAYS):

            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)
            x, y = ox, oy 

            for depth in range(int(MAX_DEPTH * 100)): 
                x += 0.01 * cos_a
                y += 0.01 * sin_a

                if (int(x), int(y)) in self.game.map.world_map:
                    pygame.draw.line(self.game.display, 'red', (ox * 100, oy * 100),
                                    (x * 100, y * 100), 2)
                    
                    pygame.draw.circle(self.game.display, 'green', (x * 100, y * 100), 5)
                    
                    break 
            ray_angle += DELTA_ANGLE

        pygame.draw.line(self.game.display, 'red', (ox * 100, oy * 100),
                        (x * 100, y * 100), 2)