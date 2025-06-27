from constants import *
from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, pos):
        super().__init__(pos.x, pos.y, SHOT_RADIUS)
        self.position = pos
        self.radius = SHOT_RADIUS
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        