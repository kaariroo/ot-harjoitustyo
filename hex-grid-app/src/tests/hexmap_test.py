import unittest
import pygame
from hexmap import Hexmap
from hexagon import Hexagon

class Testhexmap(unitteest.TestCase):
	def setUp(self):
		self.hexmap = Hexmap(600, 30, [])
		
	def test_hexlistassa_on_n_oliota(self):
		self.hexmap.make_hexmap()
		
		self.assertEqual(len(self.hexlist), 600)
		
