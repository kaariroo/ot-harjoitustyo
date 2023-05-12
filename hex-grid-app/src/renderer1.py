import pygame


class Renderer:

    """Näytön päivittämisestä vastaava luokka"""

    def __init__(self, win, picture, hexlist, dropdown):

        """Luokan konstruktori
        Args:
        win = ruutu
        hexlist = lista kuusikulmioista
        picture = ruutuun piirtyvä kuva, eli kartta
        dropdown = dropdown valikko"""

        self._win = win
        self._hexlist = hexlist
        self._picture = picture
        self._dropdown = dropdown
    

    def render(self):

        """Päivittää näytön: piirtää hexat ja jos hexa on aktiivinen, piirtää sen statblock oliot.
        Piirtää dropdown valikon """

        self._win.blit(self._picture, (0, 0))
        for hexa in self._hexlist:
            hexa.draw(self._win)
            if hexa.active:
                hexa.statblocks.draw(self._win)
            else:
                for statblock in hexa.statblocks:
                    statblock.kill()
        if self._dropdown.draw_menu:
            self._dropdown.draw(self._win)

        pygame.display.update()
