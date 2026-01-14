import pygame
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.display

        self.wall_textures = self.load_wall_textures()
        self.objects_to_draw = []

    def load_wall_textures(self):
        return {1: self.get_texture(join('assets', 'walls', '1.png'))}
    
    def get_texture(self, path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(texture, res)
    
    def draw(self):
        
        for obj in sorted(self.objects_to_draw, key=lambda n: n[0], reverse=True):
            self.screen.blit(obj[1], obj[2])
            
        self.objects_to_draw.clear()
