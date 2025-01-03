import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    SHOT_RADIUS = 5

    def __init__(self, x, y):
        super().__init__(x,y,self.SHOT_RADIUS)
        
    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="red", center=(self.x,self.y), radius=self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)
        self.x = self.position.x
        self.y = self.position.y