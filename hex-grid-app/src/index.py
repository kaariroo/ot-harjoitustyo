import pygame
from hexmap import Hexmap
from main import MainLoop
from clock import Clock
from eventqueue import EventQueue


def main():
    win = pygame.display.set_mode((1126, 926))
    picture = pygame.image.load('dndmap.jpg')
    picture = pygame.transform.scale(picture, (1126, 926))
    size = 31
    hexmap = Hexmap(600, size, [])

    pygame.display.set_caption("hexmaptool")

    event_queue = EventQueue()
    clock = Clock()
    main_loop = MainLoop(hexmap, clock, event_queue, win, picture)

    pygame.init()
    main_loop.start()


if __name__ == "__main__":
    main()
