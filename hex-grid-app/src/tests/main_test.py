import unittest
import os
import pygame
from hexagon import Hexagon
from hexmap import Hexmap
from clock import Clock
from main import MainLoop
from eventqueue import EventQueue
from renderer1 import Renderer
from dropdown import DropDown
from notes import Note

class StubEvent1:
    def __init__(self, event_type, position, button):
        self.type = event_type
        self.pos = position
        self.button = button

class StubEvent2:
    def __init__(self, event_type, position):
        self.type = event_type
        self.pos = position

class StubEventQueue:
    def __init__(self, events):
        self._events = events
    
    def get(self):
        return self._events


class Testmainloop(unittest.TestCase):
    def setup(self):
        pass

    def test_right_hex_activates(self):
        
        self.win = pygame.display.set_mode((1126, 926))
        self.picture = pygame.image.load('dndmap.jpg')
        self.picture = pygame.transform.scale(self.picture, (1126, 926))
        self.hexmap = Hexmap(600, [])
        self.clock = Clock()
        self.dropdown = DropDown(
        (100, 80, 255),
        [(255, 255, 255), (255, 230, 255)],
        1113, 0, 200, 30, 
        "Monsters", ["wolf", "owlbear", "dryad", "goblin", "goblin_boss"])
        motion = StubEvent1(pygame.MOUSEMOTION, [30,30], 3)
        click = StubEvent1(pygame.MOUSEBUTTONUP, [31,31], 3)
        quit = StubEvent2(pygame.QUIT, [0,0])
        events = [motion, click, quit]
        self.renderer = Renderer(self.win, self.picture, self.hexmap.hexlist, self.dropdown)
        self.mainloop = MainLoop(self.hexmap, self.clock, StubEventQueue(events), self.win, self.picture, self.renderer, self.dropdown)
        self.mainloop.start()

        self.assertEqual(self.hexmap.find_hex(click.pos[0], click.pos[1]), self.hexmap.hexlist[0])

    def left_click_works(self):
        
        self.win = pygame.display.set_mode((1126, 926))
        self.picture = pygame.image.load('dndmap.jpg')
        self.picture = pygame.transform.scale(self.picture, (1126, 926))
        self.hexmap = Hexmap(600, [])
        self.clock = Clock()
        
        self.dropdown = DropDown(
        (100, 80, 255),
        [(255, 255, 255), (255, 230, 255)],
        1113, 0, 200, 30, 
        "Monsters", ["wolf", "owlbear", "dryad", "goblin", "goblin_boss"])
        self.renderer = Renderer(self.win, self.picture, self.hexmap.hexlist, self.dropdown)
        motion = StubEvent1(pygame.MOUSEMOTION, [30,30], 3)
        click = StubEvent1(pygame.MOUSEBUTTONUP, [31,31], 3)
        motion2 = StubEvent1(pygame.MOUSEMOTION, [1125,925], 3)
        left_click = StubEvent1(pygame.MOUSEBUTTONUP, [1125, 925], 1)
        quit = StubEvent2(pygame.QUIT, [0,0])
        events = [motion, click, motion2, left_click, quit]
        self.mainloop = MainLoop(self.hexmap, self.clock, StubEventQueue(events), self.win, self.picture, self.renderer, self.dropdown)
        
        
        self.mainloop.start()
        

        self.assertEqual(self.mainloop.dropdown.menu_active, False)
