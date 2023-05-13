import unittest
import pygame
from dropdown import DropDown

class Testdropdown(unittest.TestCase):
    def setUp(self):
        self.dropdown = DropDown((100, 80, 255), [(255, 255, 255), (255, 230, 255)], 1113, 0, 200, 30, "Monsters", ["wolf", "owlbear", "dryad"])

    def test_draw(self):
        self.draw_menu = True
        self.menu_active = False
        self.active_option = None
        win = pygame.display.set_mode((1313, 1080))
        pygame.init()
        
        
        self.dropdown.draw(win)
        self.assertEqual(self.dropdown.rect.y, 0)
        