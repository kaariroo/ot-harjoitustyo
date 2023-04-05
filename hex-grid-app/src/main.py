import pygame
from hexagon import Hexagon

class MainLoop:
	def __init__(self, hexmap, clock, event_queue, win, bg):
		self.hexmap = hexmap
		self.clock = clock
		self.win = win
		self.bg = bg
		self.event_queue = event_queue
	
	def redraw_game_window(self):
		self.win.blit(self.bg, (0, 0))
		for hex in self.hexmap.hexlist:
			hex.draw(self.win)
		pygame.display.update()
	
	def _handle_events(self):
		for event in self.event_queue.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				clicked = hexmap.find_hex(event.pos[0], event.pos[1])
				clicked.color = (0, 0, 255)
			elif event.type == pygame.QUIT:
                		return False

	def start(self):
		
		while True:
			if self._handle_events() == False:
				break
		
			self.clock.tick(20)

			self.redraw_game_window()

		pygame.quit












#clock = pygame.time.Clock()



# piirtää kartan alle ja laittaa hexat paikoilleen
#def redraw_game_window():
#    win.blit(bg, (0, 0))
#    for hex in hex_list:
#        hex.draw()
#    pygame.display.update()

#laittaa hexat listaan
#nämä Hexmap luokassa
#hex_list = []
#for _ in range(600):
#	size = 31
#	hex_list.append(Hexagon(win, (255, 255, 255), 6, size, size, size, 1))

#muuttaa hexojen paikat kohdilleen, hexat vähän vituillaan
#hex_column = 0
#hex_row = 0
#for i in hex_list:
#    if hex_column % 2 == 0:
#        i.x += 1.5 * hex_column * i.radius
#        i.y += hex_row * (1.75 * i.radius)
#                
#    if hex_column % 2 != 0:
#        i.x += 1.5 * hex_column * i.radius
#        i.y += hex_row * (1.75 * i.radius) + (0.9 * i.radius)
#    hex_row += 1
# 
#    if hex_row >= 20:
#        hex_column += 1
#        hex_row = 0



#run = True 
#while run:
#    clock.tick(27)
#
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            run = False
        

#    redraw_game_window()

#pygame.quit
