import unittest
import pygame
from hexagon import Hexagon
from hexmap import Hexmap
from clock import Clock
from main import MainLoop
from eventqueue import EventQueue

class StubEvent1:
    def __init__(self, event_type, position):
        self.type = event_type
        self.pos = position

class StubEvent2:
    def __init__(self, event_type):
        self.type = event_type


class StubEventQueue:
    def __init__(self, events):
        self._events = events
    
    def get(self):
        return self._events


class Testmainloop(unittest.TestCase):
    def setup(self):
        pass
        
        
    def test_right_hex_activates(self):
        
        
        win = pygame.display.set_mode((1126, 926))
        picture = pygame.image.load('dndmap.jpg')
        picture = pygame.transform.scale(picture, (1126, 926))
       
        hexmap = Hexmap(600, [])
        clock = Clock()
        

        #pygame.init()

        motion = StubEvent1(pygame.MOUSEMOTION, [30,30])
        click = StubEvent1(pygame.MOUSEBUTTONDOWN, [31,31])
        quit = StubEvent2(pygame.QUIT)
        events = [motion, click, quit]
        self.mainloop = MainLoop(hexmap, clock, StubEventQueue(events), win, picture)
        self.mainloop.start()
        
        

        self.assertEqual(hexmap.find_hex(click.pos[0], click.pos[1]), hexmap.hexlist[0])