from circleshape import CircleShape
import random
from constants import ASTEROID_MIN_RADIUS
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid_1.velocity = self.velocity.rotate(angle) * 1.2
            asteroid_2.velocity = self.velocity.rotate(-angle) * 1.2

