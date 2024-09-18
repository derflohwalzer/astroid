from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        radius = self.radius - ASTEROID_MIN_RADIUS
        velocity_a = self.velocity.rotate(angle * (-1)) * ASTEROID_SPEED_MULTIPIER
        velocity_b = self.velocity.rotate(angle) * ASTEROID_SPEED_MULTIPIER
        asteroid_a = Asteroid(self.position.x, self.position.y, radius)
        asteroid_a.velocity = velocity_a 
        asteroid_b = Asteroid(self.position.x, self.position.y, radius)
        asteroid_b.velocity = velocity_b 



