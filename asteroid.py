from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="yellow", center=(self.x,self.y), radius=self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)
        self.x = self.position.x
        self.y = self.position.y
    