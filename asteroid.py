from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
import random
from logger import log_event
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position,LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self, ):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle =random.uniform(20, 50)
            vector = self.velocity.rotate(angle)
            negvector = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            small_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            med_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            small_asteroid.velocity = vector * 1.2
            med_asteroid.velocity = negvector *1.2