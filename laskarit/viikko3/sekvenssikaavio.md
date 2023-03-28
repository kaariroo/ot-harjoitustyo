```mermaid
sequenceDiagram
	participant Main
	participant kone
	participant tankki
	participant moottori
	Main->>kone: Machine()
	kone->>tankki: Fueltank()
	kone->>tankki: FuelTank.fill(40)
	kone->>moottori: Engine(tankki)
