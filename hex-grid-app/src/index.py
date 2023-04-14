import pygame
from hexagon import Hexagon
from hexmap import Hexmap
from main import MainLoop
from clock import Clock
from eventqueue import EventQueue


def main():
    win = pygame.display.set_mode((1126, 926))
    bg = pygame.image.load('dndmap.jpg')
    bg = pygame.transform.scale(bg, (1126, 926))
    size = 31
    hexagon = Hexagon((255, 255, 255), 6, 31, 31, 31, 1)
    hexmap = Hexmap(600, size, [])

    pygame.display.set_caption("hexmaptool")

    event_queue = EventQueue()
    clock = Clock()
    main_loop = MainLoop(hexmap, clock, event_queue, win, bg)

    pygame.init()
    main_loop.start()


if __name__ == "__main__":
    main()
