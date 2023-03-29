```mermaid
sequenceDiagram
	participant Main
	Main->>kone: Machine()
	participant kone
	activate kone
	kone->>tankki: kone._tank=Fueltank()
	participant tankki
	kone->>tankki: kone._tank.fill(40)
	kone->>moottori: kone._engine=Engine(kone._tank)
	participant moottori
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
