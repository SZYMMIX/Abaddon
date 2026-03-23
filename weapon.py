import pygame
from settings import *

class Weapon: 
    def __init__(self, game):
        self.game = game
        self.images = []
        self.range = 7
        
        NUM_FRAMES = 15 
        SCALE_FACTOR = 0.43 
        ANIMATION_SPEED = 5 

        try:
            for i in range(NUM_FRAMES): 
                path = join("assets", "weapons", "shotgun", f'{i}.png')
                img = pygame.image.load(path).convert_alpha()
                
                s_w = int(WIDTH * SCALE_FACTOR)
                s_h = int(s_w * (img.get_height() / img.get_width())) 
                
                img = pygame.transform.scale(img, (s_w, s_h))
                self.images.append(img)
        except:
            s = pygame.Surface((100,100)); s.fill('red')
            self.images = [s]

        self.frame_index = 0
        self.animation_speed = ANIMATION_SPEED
        self.frame_timer = 0
        self.shooting = False
        
        self.base_image = self.images[0]
        self.pos = (HALF_WIDTH - self.base_image.get_width() // 3, 
                    HEIGHT - self.base_image.get_height() // 1.3)

    def animate(self):
        if self.shooting:
            self.frame_timer += 1
            if self.frame_timer >= self.animation_speed:
                self.frame_timer = 0
                self.frame_index += 1
                
                if self.frame_index >= len(self.images):
                    self.frame_index = 0
                    self.shooting = False 
    
    def fire(self):
        if not self.shooting:
            self.shooting = True
            self.frame_index = 1 
            self.frame_timer = 0
            
            for object in self.game.object_handler.sprite_list:
                
                if not object.is_dead:
                    if object.screen_x - object.sprite_half_width < HALF_WIDTH < object.screen_x + object.sprite_half_width:
                        ray_idx = NUM_RAYS // 2
                        
                        if self.game.raycasting.depth_buffer_list:
                            wall_dist = self.game.raycasting.depth_buffer_list[ray_idx]
                            
                            if object.norm_dist < wall_dist and object.norm_dist < self.range:
                                object.health -= 50
                                
                                if object.health <= 0:
                                    object.is_dead = True
                                
                                break

    def update(self):
        keys = pygame.key.get_pressed()
        mouse_buttons = pygame.mouse.get_pressed()
        if keys[pygame.K_SPACE] or mouse_buttons[0]: 
            self.fire()
        
        self.animate()

    def draw(self):
        self.game.display.blit(self.images[self.frame_index], self.pos)