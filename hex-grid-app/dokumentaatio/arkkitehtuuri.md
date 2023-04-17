```mermaid classDiagram
Mainloop -- Hexmap
Hexmap -- Hexagon


class Hexagon{
    +draw(self)
}

class Hexmap{
    +make_hexmap(tekee listan hexoista ja asettaa ne paikoilleen)
    +find_hex(click_x, click_y)
}

class Mainloop{
    +redraw gamewindow()
    +handle_events()
    +start()
}