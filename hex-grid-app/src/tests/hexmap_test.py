import unittest
import pygame
from hexmap import Hexmap
from hexagon import Hexagon
from clock import Clock
from main import MainLoop
from eventqueue import EventQueue


class Testhexmap(unittest.TestCase):
    def setUp(self):
        self.hexmap = Hexmap(600, [])

    def test_hexlistassa_on_n_oliota(self):
        self.assertEqual(len(self.hexmap.hexlist), 600)

    def test_findhex(self):
        hexa = self.hexmap.find_hex(15, 15)

        self.assertEqual(hexa, self.hexmap.hexlist[0])

    