import pygame
import sys
from player import Player
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state,log_event
from asteroid import Asteroid
from AsteroidField import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image = pygame.image.load("/home/temme/workspace/asteroids/starbackground.jpg")
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version:{pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    asteroidfile = AsteroidField()
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    


    while True:
        log_state()
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
          print(f"quitter! you only got {score} points")
          return
        screen.fill("black")
        screen.blit(background_image, (0,0))
        updatable.update(dt)
        for asteroid in asteroids:
           if asteroid.collides_with(player):
            log_event("player_hit")
            print("Game Over!")
            print(f"you got {score} points")
            sys.exit()
            

           for bullet in shots:
             if asteroid.collides_with(bullet):
                log_event("asteroid_shot")
                bullet.kill()
                asteroid.split()
                score += 1
        for obj in drawable:
          obj.draw(screen)
        pygame.display.flip()
        result =  clock.tick(60)
        dt = result/1000
        
        


if __name__ == "__main__":
    main()
