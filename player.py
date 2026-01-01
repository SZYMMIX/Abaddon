from settings import *

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self):
        dt = self.game.clock.get_time()
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * dt
        rot_speed = PLAYER_ROT_SPEED * dt

        mx, _ = pygame.mouse.get_rel()

        if mx:
            self.angle += mx * MOUSE_SENSITIVITY
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.angle -= rot_speed
        if keys[pygame.K_RIGHT]:
            self.angle += rot_speed

        if keys[pygame.K_w]:
            dx += speed * cos_a
            dy += speed * sin_a
        if keys[pygame.K_s]:
            dx += -speed * cos_a
            dy += -speed * sin_a
        if keys[pygame.K_a]:
            dy += -speed * sin_a