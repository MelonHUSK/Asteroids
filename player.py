from circleshape import CircleShape
import pygame
from constants import PLAYER_RADIUS, PLAYER_THRUST, PLAYER_TURN_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.image = pygame.Surface((PLAYER_RADIUS * 2, PLAYER_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (PLAYER_RADIUS, PLAYER_RADIUS), PLAYER_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)