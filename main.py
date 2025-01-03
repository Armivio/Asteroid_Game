# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group,)
    clock = pygame.time.Clock()
    dt = 0

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        for updatable in updatable_group:
            updatable.update(dt)
        
        for asteroid in asteroid_group:
            if player.collidesWith(asteroid):
                print("Game over!")
                return 

        for drawable in drawable_group:
            drawable.draw(screen)
            
        pygame.display.flip()
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
