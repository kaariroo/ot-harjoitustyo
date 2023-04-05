import pygame
import math
from hexagon import Hexagon

class Hexmap():
	def __init__(self, n, size, hexlist):
		self.n = n
		self.size = size
		self.hexlist = hexlist
		self.make_hexmap()
	
	def make_hexmap(self):
		for _ in range(self.n):
			self.hexlist.append(Hexagon((255, 255, 255), 6, 31, 31, 31, 1))

#muuttaa hexojen paikat kohdilleen, hexat vähän vituillaan
		hex_column = 0
		hex_row = 0
		for i in self.hexlist:
			if hex_column % 2 == 0:
				i.x += 1.5 * hex_column * i.radius
				i.y += hex_row * (1.75 * i.radius)
                
			if hex_column % 2 != 0:
				i.x += 1.5 * hex_column * i.radius
				i.y += hex_row * (1.75 * i.radius) + (0.9 * i.radius)
			hex_row += 1
			if hex_row >= 20:
				hex_column += 1
				hex_row = 0
	
	def find_hex(self, x, y):
		result = self.hexlist[0]
		for hex in self.hexlist:
			hex.distance = math.sqrt((abs(hex.x - x))**2 + (abs(hex.y -y))**2)
			if hex.distance < result.distance:
				result = hex
		return result


