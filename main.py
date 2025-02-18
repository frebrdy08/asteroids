import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    display_clock = pygame.time.Clock()
    score = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable, shots)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player_shape = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for aa in asteroids:
            if aa.collision_detect(player_shape) == True:
                print(f"Game Over!\nYou destroyed {score} asteroids")
                sys.exit()
            for s in shots:
                if aa.collision_detect(s) == True:
                    s.kill()
                    aa.split()
                    score += 1

        screen.fill(BACKGROUND_COLOR)

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

        dt = display_clock.tick(60) / 1000


if __name__ == "__main__":
    main()