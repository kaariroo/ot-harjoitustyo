import math
from hexagon import Hexagon


class Hexmap():
    def __init__(self, amount, size, hexlist):
        self.amount = amount
        self.size = size
        self.hexlist = hexlist
        self.make_hexmap()

    def make_hexmap(self):
        for _ in range(self.amount):
            self.hexlist.append(Hexagon((255, 255, 255), 6, 31, 31, 31, 1))

# muuttaa hexojen paikat kohdilleen, hexat vähän vituillaan
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
            if hex_row >= 20:
                hex_column += 1
                hex_row = 0

    def find_hex(self, click_x, click_y):
        result = self.hexlist[0]
        for hexa in self.hexlist:
            hexa.distance = math.sqrt((abs(hex.x - click_x))**2 + (abs(hex.y - click_y))**2)
            if hex.distance < result.distance:
                result = hexa
        return result
