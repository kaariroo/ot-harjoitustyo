from math import cos, sin, pi
import pygame


class Hexagon():
    def __init__(self, color, vertex_count, radius, center_x, center_y, width):
        self.color = color
        self.vertex_count = vertex_count
        self.radius = radius
        self.center_x = center_x
        self.center_y = center_y
        self.width = width

    def draw(self, win):
        r_a = self.radius
        v_n = self.vertex_count
        d_x = self.center_x
        d_y = self.center_y
        h_p=[(d_x+r_a*cos(2*pi*i/v_n),d_y+r_a*sin(2*pi*i/v_n))for i in range(v_n)]
        pygame.draw.polygon(win,self.color,h_p,self.width)
