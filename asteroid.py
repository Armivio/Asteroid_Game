from circleshape import CircleShape
from constants import *
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="yellow", center=(self.x,self.y), radius=self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)
        self.x = self.position.x
        self.y = self.position.y
    
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS: 
            return
        random_angle = random.uniform(20, 50)
        vect1 = self.velocity.rotate(random_angle)
        vect2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.x, self.y, new_radius)
        asteroid2 = Asteroid(self.x, self.y, new_radius)
        asteroid1.velocity = vect1 * ASTEROID_ACC
        asteroid2.velocity = vect2 * ASTEROID_ACC