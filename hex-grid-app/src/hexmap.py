from math import sqrt
from hexagon import Hexagon


class Hexmap():

    """Kuusikulmioista ruudukon muodostava luokka"""
    def __init__(self, amount, hexlist):

        """Luokan konstruktori joka luo uuden ruudukon. Kutsuu make_hexmap funktiota.
        Args:
            amount: ruutujen määrä
            hexlist: tyhjä lista"""
        self.amount = amount
        self.hexlist = hexlist
        self.make_hexmap()

    def make_hexmap(self):

        """Lisää hexlistiin kostruktorissa olevan määrän hexagon olioita, 
        jonka jälkeen sijoittaa ne paikoilleen ruudukkoon
        melko tyydyttävän tiheäksi ruudukoksi."""

        for _ in range(self.amount):
            self.hexlist.append(Hexagon((255, 255, 255, 255), 6, 93, 90, 90, 1))
        hex_column = 0
        hex_row = 0
        for i in self.hexlist:
            if hex_column % 2 == 0:
                i.center_x += 1.5 * hex_column * i.radius
                i.center_y += hex_row * (1.75 * i.radius)

            if hex_column % 2 != 0:
                i.center_x += 1.5 * hex_column * i.radius
                i.center_y += hex_row * (1.75 * i.radius) + (0.9 * i.radius)
            hex_row += 1
            if hex_row >= 8:
                hex_column += 1
                hex_row = 0

    def find_hex(self, click_x, click_y):

        """Etsii minkä ruudun kohdalla hiiri kulloinkin on."""

        result = self.hexlist[0]
        for hexa in self.hexlist:
            hexa.distance=sqrt((abs(hexa.center_x-click_x))**2+(abs(hexa.center_y-click_y))**2)
            if hexa.distance < result.distance:
                result = hexa
        return result
