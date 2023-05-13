import unittest
import pygame
from statblock import Statblock


class Teststatblock(unittest.TestCase):
    def setUp(self):
        self.statblock = Statblock((0,0), "wolf")

    def test_oikean_kokoinen_kuva_latautuu(self):
        self.assertEqual(self.statblock.rect.right, 400)
        