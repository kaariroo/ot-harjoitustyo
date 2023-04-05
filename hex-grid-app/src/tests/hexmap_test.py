import unittest
import pygame
from hexmap import Hexmap
from hexagon import Hexagon

class Testhexmap(unittest.TestCase):
	def setUp(self):
		self.hexmap = Hexmap(600, 30, [])
		
	def test_hexlistassa_on_n_oliota(self):
		self.assertEqual(len(self.hexmap.hexlist), 600)
		
