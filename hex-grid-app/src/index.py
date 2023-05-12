import pygame
from hexmap import Hexmap
from main import MainLoop
from clock import Clock
from eventqueue import EventQueue
from renderer1 import Renderer
from dropdown import DropDown


def main():
    win = pygame.display.set_mode((1313, 1080))
    picture = pygame.image.load('dndmap.jpg')
    picture = pygame.transform.scale(picture, (1313, 1080))
    hexmap = Hexmap(80, [])
    dropdown = DropDown(
    (100, 80, 255),
    [(255, 255, 255), (255, 230, 255)],
    1113, 0, 200, 30, 
    "Monsters", ["wolf", "owlbear", "dryad", "goblin", "goblin_boss"])
    renderer = Renderer(win, picture, hexmap.hexlist, dropdown)

    pygame.display.set_caption("hexmaptool")

    event_queue = EventQueue()
    clock = Clock()
    main_loop = MainLoop(hexmap, clock, event_queue, win, picture, renderer, dropdown)

    pygame.init()
    main_loop.start()

if __name__ == "__main__":
    main()
