import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    astroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (astroids,updateable,drawable)
    Shot.containers = (shots, updateable, drawable)
    AsteroidField.containers = (updateable)
    player = Player(x= SCREEN_WIDTH / 2, y= SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updateable.update(dt)
        for obj in astroids:
            if obj.collision_check(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if obj.collision_check(shot):
                    obj.split()
                    shot.kill()
        screen.fill((0,0,0))

        for obj in drawable:
            obj.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
