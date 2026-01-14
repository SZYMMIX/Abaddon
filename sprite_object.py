import pygame
import math
from settings import *

class SpriteObject:
    def __init__(self, game, path, pos, scale=1, shift=0.2):
        self.game = game
        self.x, self.y = pos
        self.image = pygame.image.load(path).convert_alpha()

        self.IMAGE_WIDTH = self.image.get_width()
        self.IMAGE_HALF_WIDTH = self.IMAGE_WIDTH // 2
        self.IMAGE_RATIO = self.IMAGE_WIDTH / self.image.get_height()

        self.scale = scale
        self.shift = shift

        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.norm_dist = 0, 0, 0, 0, 1, 1
        self.sprite_half_width = 0

    def get_sprite_projection(self):
        # proj = self.game.raycasting.proj_height

        dx = self.x - self.game.player.x
        dy = self.y - self.game.player.y
        self.dx, self.dy = dx, dy

        self.theta = math.atan2(dy, dx)
        delta = self.theta - self.game.player.angle

        if (dx > 0 and self.game.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau

        delta_rays = delta / DELTA_ANGLE
        self.screen_x = (NUM_RAYS / 2 + delta_rays) * SCALE

        self.dist = math.hypot(dx, dy)
        
        self.norm_dist = self.dist * math.cos(delta)
        
        if -self.IMAGE_HALF_WIDTH < self.screen_x < (WIDTH + self.IMAGE_HALF_WIDTH) and self.norm_dist > 0.5:
            self.get_sprite()

    def get_sprite(self):
        proj_height = SCREEN_DIST / self.norm_dist * self.scale
        proj_width = proj_height * self.IMAGE_RATIO
        proj_height, proj_width = int(proj_height), int(proj_width)

        image = pygame.transform.scale(self.image, (proj_width, proj_height))
        
        self.sprite_half_width = proj_width // 2
        
        height_shift = proj_height * self.shift
        pos = (self.screen_x - self.sprite_half_width, 
               HEIGHT // 2 - proj_height // 2 + height_shift)

        self.game.object_renderer.objects_to_draw.append((self.norm_dist, image, pos))


    def update(self):
        self.get_sprite_projection()