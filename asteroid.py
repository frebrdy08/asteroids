import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_COLOR, self.position, self.radius, ASTEROID_LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        old_radius = self.radius
        old_velocity = self.velocity
        self.kill()
        old_position = self.position
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            dir_a = old_velocity.rotate(angle)
            dir_b = old_velocity.rotate(-angle)
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            new_asteroid_a = Asteroid(old_position.x, old_position.y, new_radius)
            new_asteroid_a.velocity = dir_a * FRAGMENT_ACCELERATION
            new_asteroid_b = Asteroid(old_position.x, old_position.y, new_radius)
            new_asteroid_b.velocity = dir_b * FRAGMENT_ACCELERATION
