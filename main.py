import pygame
from constants import *
from player import Player


def main():
    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for unit in drawable:
            unit.draw(screen)
        for unit in updatable:
            unit.update(dt)
        # player.update(dt)
        # player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
