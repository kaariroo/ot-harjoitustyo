from math import cos, sin, pi
import pygame


class Hexagon():

    """Yksittäisen kuusikulmion luomisesta vastaava luokka"""

    def __init__(self, color, vertex_count, radius, center_x, center_y, width):

        """Luokan konstrukstori joka luo uuden kuusikulmion.
        
        Args:
            color: väri
            vertex_count: kulmien määrä
            radius: säde
            center_x: keskustan x koordinaatti
            center_y: keskustan y koordinaatti
            width: reunan paksuus"""
        self.color = color
        self.vertex_count = vertex_count
        self.radius = radius
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.statblocks = pygame.sprite.Group()
        self.active = False

    def draw(self, win):

        """Kuusikulmion piirtävä metodi. Saa argumentin win, eli ohjelman ikkunan. 
        h_p laskee kulmien paikat ja käyttää pygamen draw.polygon funktiota."""

        r_a = self.radius
        v_n = self.vertex_count
        d_x = self.center_x
        d_y = self.center_y
        h_p=[(d_x+r_a*cos(2*pi*i/v_n),d_y+r_a*sin(2*pi*i/v_n))for i in range(v_n)]
        pygame.draw.polygon(win,self.color,h_p,self.width)
