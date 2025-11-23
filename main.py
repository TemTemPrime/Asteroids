import pygame
import sys
from player import Player
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state,log_event
from asteroid import Asteroid
from AsteroidField import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version:{pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    

    
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfile = AsteroidField()
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    


    while True:
        log_state()
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
          return
        screen.fill(" black")
        updatable.update(dt)
        for asteroid in asteroids:
           if player.collides_with(asteroid) == True:
            log_event("player_hit")
            print("Game Over!")
            sys.exit()
        for obj in drawable:
          obj.draw(screen)
        pygame.display.flip()
        result =  clock.tick(60)
        dt = result/1000
        
        


if __name__ == "__main__":
    main()
