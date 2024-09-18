import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField
from shot import Shot
def main():
    # INIT
    pygame.init()

    # Parameters
    clock = pygame.time.Clock()
    dt = 0
    
    # Groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # Add Classes to Group
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)
    # Create Objects
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    asteroidField = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    # Gameplay Loop
    while(True):
        # Close the window when player quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        for object in updatables:
            object.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.checkCollision(shot):
                    asteroid.split()
                    shot.kill()

            if player.checkCollision(asteroid):
                print("Game over!")
                return
            
        for object in drawables:
            object.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()