```mermaid
sequenceDiagram
	participant Main
	participant kone
	participant tankki
	participant moottori
	Main->>kone: Machine()
	activate kone
	kone->>tankki: Fueltank()
	kone->>tankki: FuelTank.fill(40)
	kone->>moottori: Engine(tankki)
	kone->>Main
	deactivate kone
