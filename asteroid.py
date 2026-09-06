import pygame
import random

from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.image = pygame.transform.smoothscale(random.choice(Asteroid.images), (int(radius * 2), int(radius * 2)))
        self.spin = random.uniform(-90, 90)
        self.angle = random.uniform(0, 360)

    def draw(self, screen):
        center = self.position
        rotated = pygame.transform.rotate(self.image, self.angle)
        screen.blit(rotated, rotated.get_rect(center=center))

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)
        self.angle = self.angle + (self.spin * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random.uniform(20, 50)
            new_vector = self.velocity
            rotated_vector = new_vector.rotate(random.uniform(20, 50))
            second_rotated_vector = new_vector.rotate(random.uniform(20, 50)) * -1
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = rotated_vector * 1.2
            new_asteroid2.velocity = second_rotated_vector * 1.2
