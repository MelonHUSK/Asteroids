import pygame 
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidsfield import AsteroidField

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")

    asteroids = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)

    asteroidField = AsteroidField()
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

        updatables.update(dt)

        for i in asteroids:
            if i.check_collision(player) == True:
                print("Game Over")
                running = False

        for i in drawables:
            i.draw(screen)

        pygame.display.flip()
        game_clock.tick(60)
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
