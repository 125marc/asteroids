import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock_set = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers=(shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Player.containers= (drawable, updatable)
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black", rect=None, special_flags=0)
        dt = clock_set.tick(60)/1000
        for asteroid in asteroids:
            if player.collisions(asteroid):
                print("Game over!")
                pygame.QUIT
                return
            for shot in shots:
                if shot.collisions(asteroid):
                    shot.kill()
                    asteroid.split()
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        
        





if __name__ == "__main__":
    main()