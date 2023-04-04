import pygame
from hexagon import Hexagon
from hexmap import Hexmap
from main import MainLoop
from clock import Clock

def main():
	win = pygame.display.set_mode((1024, 842))
	bg = pygame.image.load('dndmap.jpg')
	bg = pygame.transform.scale(bg, (1024, 842))
	size = 31
	hexagon = Hexagon((255, 255, 255), 6, 31, 31, 31, 1)
	hexmap = Hexmap(600, size, [])
	
	
	pygame.display.set_caption("hexmaptool")
	
	clock = Clock()
	main_loop = MainLoop(hexmap, clock, win, bg)
	
	pygame.init()
	main_loop.start()
	

if __name__ == "__main__":
    main()
