import os
import pygame
from notes import Note
from monster_notes import MonsterNote
from statblock import Statblock
from dropdown import DropDown



class MainLoop:

    """Ohjelman pääsilmukasta vastaava luokka."""

    def __init__(self, hexmap, clock, event_queue, win, picture, renderer, dropdown):

        """Luokan konstruktori joka luo uuden silmukan.
        Args:
            hexmap: kuusikulmioista muodostettu ruudukko
            clock: kello
            win: pelin ikkuna
            picture: peli-ikkunaan pohjalle tuleva kuva
            event_queue: tapahtumajono"""

        self.hexmap = hexmap
        self.clock = clock
        self.win = win
        self.picture = picture
        self.event_queue = event_queue
        self.renderer = renderer
        self.aimedhex = self.hexmap.hexlist[0]
        self.dropdown =  dropdown
        self.active = None
        self.clicked = None

    def handle_events(self):

        """Käsittelee näppäimistöllä annettavat tapahtumat"""
        left = 1
        right = 3
        
        for event in self.event_queue.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == left and not self.dropdown.draw_menu:
                    self.clicked = self.hexmap.find_hex(event.pos[0], event.pos[1])
                    self.clicked.color = (250, 235, 215, 255)
                    notes = Note(self.clicked)
                    notes.write(self.hexmap.hexlist.index(self.clicked))
                    self.clicked.width = 1
                    return True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == left and self.dropdown.draw_menu is True:
                    self.dropdown.update()
                    if self.dropdown.active_option is not None:
                        active_monster = self.dropdown.monsters[self.dropdown.active_option]
                    if self.dropdown.active_option is not None:
                        if len(self.active.statblocks.sprites()) == 0:
                            monster_note = MonsterNote(self.active, active_monster)
                            monster_note.write(self.hexmap.hexlist.index(self.active))
                            statblock = Statblock((0,0), active_monster)
                            self.active.statblocks.add(statblock)
                        elif self.active.statblocks.sprites()[-1].rect.right > 750:
                            if self.active.statblocks.sprites()[-1].rect.top == 0:
                                monster_note = MonsterNote(self.active, active_monster)
                                monster_note.write(self.hexmap.hexlist.index(self.active))
                                pos = self.active.statblocks.sprites()[0].rect.bottomleft
                                statblock = Statblock((pos), active_monster)
                                self.active.statblocks.add(statblock)
                            else:
                                monster_note = MonsterNote(self.active, active_monster)
                                monster_note.write(self.hexmap.hexlist.index(self.active))
                                pos = self.active.statblocks.sprites()[-1].rect.topright
                                statblock = Statblock((pos), active_monster)
                                self.active.statblocks.add(statblock)
                    if self.dropdown.menu_active:
                        self.clicked.active = False
                        self.active = None
                        self.dropdown.active_option = None
                        self.dropdown.draw_menu = False
                        for hexa in self.hexmap.hexlist:
                            hexa.width = 1
            if event.type == pygame.MOUSEBUTTONUP and event.button == right:
                self.clicked = self.hexmap.find_hex(event.pos[0], event.pos[1])
                self.clicked.color = (250, 235, 215, 255)
                if not self.clicked.active:
                    self.clicked.active = True
                    self.active = self.clicked
                    self.clicked.width = 6
                    self.dropdown.draw_menu = True
                    dirname = os.path.dirname(__file__)
                    m_name = self.hexmap.hexlist.index(self.active)
                    monsternote_file_path = os.path.join(dirname, "monster_notes", f"{m_name}.csv")
                    if os.path.isfile( monsternote_file_path):
                        with open(monsternote_file_path) as document:
                            for text in document:
                                monsters = text.split(";")
                            monsterlist = []
                            for monster in monsters:
                                monsterlist.append(monster)
                            monsterlist.pop(-1)
                            singleslist = [*set(monsterlist)]
                            for monster in singleslist:
                                if monster == singleslist[0]:
                                    statblock = Statblock((0,0), monster)
                                    self.active.statblocks.add(statblock)
                                elif self.active.statblocks.sprites()[-1].rect.right > 750:
                                    pos = self.active.statblocks.sprites()[0].rect.bottomleft
                                    statblock = Statblock((pos), monster)
                                    self.active.statblocks.add(statblock)
                                else:
                                    pos = self.active.statblocks.sprites()[-1].rect.topright
                                    statblock = Statblock((pos), monster)
                                    self.active.statblocks.add(statblock)
                elif self.clicked.active:
                    self.clicked.active = False
                    self.active = None
                    self.dropdown.draw_menu = False
                    self.dropdown.active_option = None
            if event.type == pygame.MOUSEMOTION:
                self.aimedhex = self.hexmap.find_hex(event.pos[0], event.pos[1])
                if not self.aimedhex.active:
                    self.aimedhex.color = (250, 235, 215, 255)
                    self.aimedhex.width = 4
                for hexa in self.hexmap.hexlist:
                    if hexa != self.aimedhex and not hexa.active:
                        hexa.color = (250, 235, 215, 255)
                        hexa.width = 1
    def _render(self):

        """Käynnistää rendererin joka päivittää näkymää"""

        self.renderer.render()

    def start(self):

        """Käynnistää ohjelman pääsilmukan"""

        while True:
            if self.handle_events() is False:
                break
            self.clock.tick(20)
            self._render()
        pygame.quit()
