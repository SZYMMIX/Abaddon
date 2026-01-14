from sprite_object import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.add_sprite(SpriteObject(game, path='assets/enemies/demon/walk/0.png', pos=(10.5, 5.5)))

    def update(self):
        for sprite in self.sprite_list:
            sprite.update()

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)