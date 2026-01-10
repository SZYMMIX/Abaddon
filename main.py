import pygame
import sys
from settings import *
from map import *
from player import *
from raycasting import *

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

    def update(self):
        self.player.update()
        self.raycasting.update()
        pygame.display.flip()
        self.clock.tick(FPS)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.display.fill('black')
        # self.map.draw()
        # self.player.draw()

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