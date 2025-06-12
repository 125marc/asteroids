from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x 
        self.y = y
        self.radius = radius


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        ran_angle = random.uniform(20,50)
        print("Original velocity:", self.velocity) 
        vect_one = self.velocity.rotate(ran_angle)
        vect_two = self.velocity.rotate(-ran_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_one.velocity = vect_one * 1.2
        asteroid_two.velocity = vect_two * 1.2
        






        



