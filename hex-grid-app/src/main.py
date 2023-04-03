import pygame
from hexagon import Hexagon
pygame.init()

win = pygame.display.set_mode((1024, 842))

pygame.display.set_caption("hexmaptool")

bg = pygame.image.load('dndmap.jpg')
bg = pygame.transform.scale(bg, (1220, 1000))


clock = pygame.time.Clock()




def redraw_game_window():
    win.blit(bg, (0, 0))
    for hex in hex_list:
        hex.draw()
    pygame.display.update()

#mainloop
hex_list = []
for _ in range(600):
    hex_list.append(Hexagon(win, (255, 255, 255), 6, 200, 0, 0, 1))


hex_column = 0
hex_row = 0
for i in hex_list:
    if hex_column % 2 == 0:
        i.x = 1.5 * hex_column * i.radius
        i.y = hex_row * (1.75 * i.radius)
                
    if hex_column % 2 != 0:
        i.x = 1.5 * hex_column * i.radius
        i.y = hex_row * (1.75 * i.radius) + (0.9 * i.radius)
    hex_row += 1
    if hex_row >= 20:
        hex_column += 1
        hex_row = 0



run = True 
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        

    redraw_game_window()

pygame.quit
