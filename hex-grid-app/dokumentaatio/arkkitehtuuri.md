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

```
```mermaid
sequenceDiagram

participant Main
participant MainLoop
participant Hexmap
participant Hexagon
participant Note

Main->>Hexmap: make n size hexmap
Hexmap->>Hexagon: hexmap.hexlist.append(n x hexagon)
Hexagon->>Hexmap: n x Hexagons
Hexmap->>Main: hexmap
Main->>MainLoop: hexmap, clock, event_queue, win, picture

Main->>MainLoop: start
MainLoop->>Hexagon:for i in hexmap.hexlist -> draw
Hexagon->>MainLoop: 
