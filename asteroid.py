from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random


class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
	
	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, 2)

	def update(self, dt):
		self.position += self.velocity * dt
	
	def split(self):
		self.kill()
		
		if (self.radius) <= ASTEROID_MIN_RADIUS:
			return
		
		split_angle = random.uniform(20, 50)
		new_velocities = [
			self.velocity.rotate(split_angle),
			self.velocity.rotate(-split_angle)
		]
		new_radius = self.radius - ASTEROID_MIN_RADIUS
		for v in new_velocities:
			asteroid = Asteroid(
				self.position.x,
				self.position.y,
				new_radius
			)
			asteroid.velocity = v * 1.2
