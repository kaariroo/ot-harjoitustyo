import pygame
import math

class Hexagon(pygame.sprite.Sprite):
	def __init__(self, surface, color, vertex_count, radius, x, y, width):
		self.surface = surface
		self.color = color
		self.vertex_count = vertex_count
		self.radius = radius
		self.x = x
		self.y = y
		self.width = width
	
	def draw(self):
		r = self.radius
		n = self.vertex_count
		x = self.x
		y = self.y
		pygame.draw.polygon(self.surface, self.color, [(x + r * math.cos(2 * math.pi * i / n), y + r * math.sin(2 * math.pi * i / n))for i in range(n)], self.width)
    
