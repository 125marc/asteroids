from constants import *
from circleshape import CircleShape
import pygame
import player

class Shield(CircleShape):
    def __init__(self, pos):
        super().__init__(pos.x, pos.y, SHIELD_RADIUS)
        self.position = pos
        self.radius = SHIELD_RADIUS
        self.rotation = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, "Green", self.position, self.radius, 3)
    
    def update(self, dt):
        self.position += self.position * dt