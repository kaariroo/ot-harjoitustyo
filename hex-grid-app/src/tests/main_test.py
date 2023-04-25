import unittest
import pygame
from hexagon import Hexagon
from hexmap import Hexmap
from clock import Clock
from main import MainLoop
from eventqueue import EventQueue

class StubEvent:
    def __init__(self, event_type, pos):
        self.type = event_type
        self.pos = pos


class StubEventQueue:
    def __init__(self, events):
        self._events = events


#class Testmainloop(unittest.TestCase):
    def setup(self):
        pass
        
        
    #def test_whathappens(self):
         
        events = [StubEvent(pygame.MOUSEBUTTONDOWN, (31,31)), StubEvent(pygame.QUIT, (0,0))]
        win = pygame.display.set_mode((1126, 926))
        picture = pygame.image.load('dndmap.jpg')
        picture = pygame.transform.scale(picture, (1126, 926))
        size = 31
        hexmap = Hexmap(600, size, [])
        clock = Clock()
        self.mainloop = MainLoop(hexmap, clock, StubEventQueue(events), win, picture)

        self.mainloop.start()

        self.assertEqual(hexmap.find_hex(event.pos[0], event.pos[1]), hexmap.hexlist[0])