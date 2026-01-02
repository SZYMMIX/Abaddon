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
            dx += speed * sin_a
            dy += -cos_a * speed
        if keys[pygame.K_d]:
            dx += -speed * sin_a
            dy += cos_a * speed
        
        self.x += dx
        self.y += dy
        self.angle %= math.tau

    def draw(self):
        pygame.draw.circle(self.game.display, 'green', (self.x * 100, self.y * 100), 15)
        pygame.draw.line(self.game.display, 'yellow', (self.x * 100, self.y * 100), 
                         (self.x * 100 + WIDTH * math.cos(self.angle),
                           self.y * 100 + HEIGHT * math.sin(self.angle)), 2)

    def update(self):
        self.movement()