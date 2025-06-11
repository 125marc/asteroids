import pygame
from constants import *
from player import Player
def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock_set = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black", rect=None, special_flags=0)
        clock_set.tick(60)
        dt = clock_set.tick(60) / 1000
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        
        





if __name__ == "__main__":
    main()