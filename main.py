import pygame 
from constants import *
from player import Player

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting Asteroids!")
    print(f"Screen Width: {SCREEN_WIDTH}")
    print(f"Screen Height: {SCREEN_HEIGHT}")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        game_clock.tick(60)
        dt = pygame.time.get_ticks() / 1000

if __name__ == "__main__":
    main()
