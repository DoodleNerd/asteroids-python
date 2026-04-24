import sys
import random
import pygame
from constants import *
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot
def main():
    pygame.init() 
    timer = pygame.time.Clock() 
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable) 
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField() 
    print("Starting Asteroids with pygame version: {}".format(pygame.version.ver)) 
    print("Screen width: {}".format(SCREEN_WIDTH)) 
    print("Screen height: {}".format(SCREEN_HEIGHT)) 
    screen = pygame.display.set_mode((1280, 720)) 
    while (True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return
        dt = timer.tick(60) / 1000
        screen.fill('black')
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
        for drawing in drawable:
            drawing.draw(screen)
        pygame.display.flip()
        
        
if __name__ == "__main__":
    main()
