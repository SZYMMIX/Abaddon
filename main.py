import pygame
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from weapon import *
from object_handler import *
from object_renderer import *

class Game:
    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.running = True
        self.new_game()

        pygame.mouse.set_visible(False) 
        pygame.event.set_grab(True)


    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.raycasting = RayCasting(self)
        self.weapon = Weapon(self)
        self.object_renderer = ObjectRenderer(self)
        self.object_handler = ObjectHandler(self)

    def update(self):
        self.player.update()
        self.weapon.update()
        self.clock.tick(FPS)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        pygame.draw.rect(self.display, CEILING_COLOR, (0, 0, WIDTH, HEIGHT // 2))
        pygame.draw.rect(self.display, FLOOR_COLOR, (0, HEIGHT // 2, WIDTH, HEIGHT // 2))
        self.raycasting.update()
        self.object_handler.update()
        self.object_renderer.draw()
        self.weapon.draw()
        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
    
    def run(self):
        while self.running:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()