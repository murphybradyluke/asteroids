import pygame

from locale import D_T_FMT

from constants import LINE_WIDTH
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        center = self.position
        radius = self.radius
        pygame.draw.circle(screen, "white", center, radius, LINE_WIDTH)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)
