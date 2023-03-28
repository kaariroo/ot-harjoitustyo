```mermaid
sequenceDiagram
	participant Main
	participant kone
	participant FuelTank
	participant Engine
	Main->>kone: Machine()
	kone->>FuelTank()
	kone->>FuelTank.fill(40)
	kone->>Engine(tank)
