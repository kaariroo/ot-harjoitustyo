import pygame

class DropDown():
    def __init__(self, heading_color, option_color, pos_x, pos_y, width, height, main, monsters):
        self.heading_color = heading_color
        self.option_color = option_color
        self.rect = pygame.Rect(pos_x, pos_y, width, height)
        self.main = main
        self.monsters = monsters
        self.draw_menu = False
        self.menu_active = False
        self.active_option = None
    def draw(self, surf):
        pygame.draw.rect(surf, self.heading_color, self.rect, 0)
        self.font = pygame.font.Font('freesansbold.ttf', 30)
        msg = self.font.render(self.main, 1, (0, 0, 0))
        surf.blit(msg, msg.get_rect(center = self.rect.center))

        if self.draw_menu:
            for i, text in enumerate(self.monsters):
                rect = self.rect.copy()
                rect.y += (i+1) * self.rect.height
                pygame.draw.rect(surf,self.option_color[1 if i == self.active_option else 0],rect,0)
                msg = self.font.render(text, 1, (0, 0, 0))
                surf.blit(msg, msg.get_rect(center = rect.center))
    def update(self):
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)
        for i in range(len(self.monsters)):
            rect = self.rect.copy()
            rect.y += (i+1) * self.rect.height
            if rect.collidepoint(mpos):
                self.active_option = i
                break
            self.active_option = None
