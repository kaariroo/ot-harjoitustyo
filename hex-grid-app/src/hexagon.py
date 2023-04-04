import pygame
import math

class Hexagon():
	def __init__(self, color, vertex_count, radius, x, y, width):
		self.color = color
		self.vertex_count = vertex_count
		self.radius = radius
		self.x = x
		self.y = y
		self.width = width
	
	def draw(self, win):
		r = self.radius
		n = self.vertex_count
		x = self.x
		y = self.y
		#print("drawing", r, n, x, y)
		pygame.draw.polygon(win, self.color, [(x + r * math.cos(2 * math.pi * i / n), y + r * math.sin(2 * math.pi * i / n))for i in range(n)], self.width)
    
