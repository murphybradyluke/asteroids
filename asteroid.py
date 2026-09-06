import pygame
import random

from locale import D_T_FMT

from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.color = self.random_color()

    @staticmethod
    def random_color() -> pygame.Color:
        # random hue at full saturation/brightness so it stands out on black
        color = pygame.Color(0)
        color.hsva = (random.uniform(0, 360), 100, 100, 100)
        return color

    def draw(self, screen):
        center = self.position
        radius = self.radius
        pygame.draw.circle(screen, self.color, center, radius, LINE_WIDTH)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

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
