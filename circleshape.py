import pygame
import math
import constants

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def collisions(self, other_circle, shield=False):
        dist = math.hypot(other_circle.position.x - self.position.x, other_circle.position.y - self.position.y)
        if shield:
            if int(dist) <= 35 + other_circle.radius:
                return True
        elif int(dist) <= (self.radius -3) + other_circle.radius:
            return True
        else:
            return False