```mermaid
classDiagram

Mainloop -- Hexmap
Hexmap -- Hexagon
Mainloop -- Note
Note -- Hexagon

class Hexagon{
    +draw(self)
}

class Hexmap{
    +make_hexmap(tekee listan hexoista ja asettaa nepaikoilleen)
    +find_hex(click_x, click_y)
}

class Mainloop{
    +redraw gamewindow()
    +handle_events()
    +start()
}

class Note{
    +hexagon
    +write(avaa .txt tiedoston, johon voi kirjoittaa)
}


```mermaid

sequenceDiagram
participant Mainloop
participant Hexagon
participant Hexmap
Mainloop->>Hexmap: redraw gamewindow
