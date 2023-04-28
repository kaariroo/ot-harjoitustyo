import sys
import pygame
from notes import Note
from statblock import Statblock



class MainLoop:
    def __init__(self, hexmap, clock, event_queue, win, picture):
        self.hexmap = hexmap
        self.clock = clock
        self.win = win
        self.picture = picture
        self.event_queue = event_queue
        self.statblocks = pygame.sprite.Group()
        

    def redraw_game_window(self):
        self.win.blit(self.picture, (0, 0))
        for i in self.hexmap.hexlist:
            i.draw(self.win)
        pygame.display.update()

    def handle_events(self):
        LEFT = 1
        RIGHT = 3
        for event in self.event_queue.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEMOTION:
                aimedhex = self.hexmap.find_hex(event.pos[0], event.pos[1])
                aimedhex.color = (250, 235, 215, 255)
                aimedhex.width = 4
                for hexa in self.hexmap.hexlist:
                    if hexa != aimedhex:
                        hexa.color = (250, 235, 215, 255)
                        hexa.width = 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = self.hexmap.find_hex(event.pos[0], event.pos[1])
                clicked.color = (250, 235, 215, 255)
                clicked.width = 6
            if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                clicked = self.hexmap.find_hex(event.pos[0], event.pos[1])
                clicked.color = (250, 235, 215, 255)
                notes = Note(clicked)
                notes.write(self.hexmap.hexlist.index(clicked))
                clicked.width = 1
                return True
            if event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT:
                clicked = self.hexmap.find_hex(event.pos[0], event.pos[1])
                clicked.color = (250, 235, 215, 255)
                self.statblock = Statblock(0, 0, clicked, "wolf")
                self.statblocks.add(statblock)
                self.statblocks.draw(self.win)
    def start(self):
        while True:
            if self.handle_events() is False:
                break
            
            self.clock.tick(20)

            self.redraw_game_window()
        
        pygame.quit()
