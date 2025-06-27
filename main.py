import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from shield import Shield 

def main():
    print("Starting Asteroids!")
    pygame.init()
    pygame.font.init()
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
    Shield.containers = (drawable, updatable)
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    score_counter = 0
    field = AsteroidField()
    shot_counter = 0
    shield = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black", rect=None, special_flags=0)
        #Draw the score in the top right corner and update
        score_text = SCORE_FONT.render("Score: " + str(score_counter), 1, (255,165,0))
        screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - 10, 10))
        dt = clock_set.tick(60)/1000
        for asteroid in asteroids:
            if player.collisions(asteroid, shield):
                if shield:
                    asteroid.kill()
                    shield = False
                else:
                    game_over(screen)
                    return
            for shot in shots:
                if shot.collisions(asteroid):
                    shot_counter += 1
                    score_counter += 5
                    shot.kill()
                    asteroid.split()
                    if shot_counter == 10:
                        shield = True
                        shot_counter = 0
        updatable.update(dt)
        for item in drawable:
            if item == player and shield == True:
                item.draw(screen, True)
            else:
                item.draw(screen)
        pygame.display.flip()

def game_over(screen):
    game_over_txt = FONT.render("GAME OVER", True, (200, 10, 10))
    text_rect_center = game_over_txt.get_rect(center = screen.get_rect().center)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return
        screen.blit(game_over_txt, text_rect_center) 
        pygame.display.update()
    pygame.quit()
        
        





if __name__ == "__main__":
    main()