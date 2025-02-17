# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ASTEROID_KINDS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPAWN_RATE,
    BACKGROUND_COLOR
)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    while True:
        screen.fill(BACKGROUND_COLOR)
        pygame.display.flip()


if __name__ == "__main__":
    main()