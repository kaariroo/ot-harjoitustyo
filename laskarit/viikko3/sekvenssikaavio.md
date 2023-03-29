```mermaid
sequenceDiagram
	participant Main
	participant kone
	participant tankki
	participant moottori
	Main->>kone: Machine()
	activate kone
	kone->>tankki: kone._tank=Fueltank()
	kone->>tankki: kone._tank.fill(40)
	kone->>moottori: kone._engine=Engine(kone._tank)
	kone-->>Main:  
	deactivate kone
	
	Main->>kone: kone.drive()
	activate kone
	kone->>moottori: kone._engine.start()
	activate moottori
	moottori->>tankki: kone._fuel_tank.consume(5)
	deactivate moottori
	tankki->>tankki: kone._fuel_contents = 35
	kone->>moottori: kone._engine.is_running()
	activate moottori
	moottori->>kone: True
	deactivate moottori
	kone->>moottori: kone._engine.use_energy()
	activate moottori
	moottori->>tankki: kone._fuel_tank.consume(10)
	deactivate moottori
	tankki->>tankki: kone._fuel_contents = 25
	kone-->>Main:
	deactivate kone
