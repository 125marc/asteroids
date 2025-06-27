from constants import *
from circleshape import CircleShape
import pygame
from shot import Shot
import time
from shield import Shield
#from main import screen

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.rotation = 0
        self.timer = 0
        self.shield_radius = SHIELD_RADIUS
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen, shield=False):
        pygame.draw.polygon(screen, "green", self.triangle(), 2)
        if shield:
            pygame.draw.circle(screen, "yellow", self.position, self.shield_radius, 3)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.timer != 0:
            self.timer -= dt
        if keys[pygame.K_a]:
            self.rotate(-1 * dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-1 * dt)
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()
            self.timer = PLAYER_SHOOT_COOLDOWN


    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        pos = self.position.copy()
        new_shot = Shot(pos)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        new_shot.velocity = forward * PLAYER_SHOT_SPEED

        

