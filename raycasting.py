import pygame
import math
from settings import *

class RayCasting:
    def __init__(self, game):
        self.game = game

        self.textures = {
            1: pygame.image.load(join('assets', 'walls', '1.png')).convert_alpha()
        }

    def update(self):
        self.ray_cast()

    def ray_cast(self):
        ox, oy = self.game.player.x, self.game.player.y
        map_x, map_y = int(ox), int(oy)

        ray_angle = self.game.player.angle - HALF_FOV
        
        for ray in range(NUM_RAYS):

            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            y_hor, dy = (map_y + 1, 1) if sin_a > 0 else (map_y - 1e-6, -1)
            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.world_map:
                    texture_hor = self.game.map.world_map[tile_hor]
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            x_vert, dx = (map_x + 1, 1) if cos_a > 0 else (map_x - 1e-6, -1)
            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.world_map:
                    texture_vert = self.game.map.world_map[tile_vert]
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth
                
            if depth_vert < depth_hor:
                depth, texture = depth_vert, texture_vert
                y_vert %= 1
                offset = y_vert if cos_a > 0 else (1 - y_vert)
            else:
                depth, texture = depth_hor, texture_hor
                x_hor %= 1
                offset = (1 - x_hor) if sin_a > 0 else x_hor

            depth *= math.cos(self.game.player.angle - ray_angle)

            proj_height = SCREEN_DIST / (depth + 0.0001)

            wall_column = self.textures[texture].subsurface(
                offset * (TEXTURE_SIZE - SCALE), 0, SCALE, TEXTURE_SIZE
            )
            
            wall_column = pygame.transform.scale(wall_column, (SCALE, int(proj_height)))
            
            self.game.display.blit(wall_column, 
                                   (ray * SCALE, HEIGHT // 2 - proj_height // 2))

            ray_angle += DELTA_ANGLE