```mermaid
sequenceDiagram
	participant main
	participant laitehallinto
	participant rautatietori
	participant ratikka6
	participant bussi244
	
	main->>laitehallinto: HKLLaitehallinto()
	main->>rautatietori: Lataajalaite()
	main->>ratikka6: Lukijalaite()
	main->>bussi244: Lukijalaite()
	main->>laitehallinto: lisaa_lataaja(rautatietori)
	main->>laitehallinto: lisaa_lukija(ratikka6)
	main->>laitehallinto: lisaa_lukija(bussi244)
	
	participant lippu_luukku
	main->>lippu_luukku: Kioski()
	participant kallen_kortti
	main->>lippu_luukku: osta_matkakortti("Kalle")
	activate lippu_luukku
	lippu_luukku->>kallen_kortti: Matkakortti("Kalle")
	deactivate lippu_luukku
	
	main->>rautatietori: lataa_arvoa(kallen_kortti, 3)
	activate rautatietori
	rautatietori->>kallen_kortti: kasvata_arvoa(3)
	deactivate rautatietori
	activate kallen_kortti
	kallen_kortti->>kallen_kortti: kallen_kortti.arvo = 3
	deactivate kallen_kortti

	main->>ratikka6: osta_lippu(kallen_kortti, 0)
	activate ratikka6
	ratikka6->>kallen_kortti: arvo()
	activate kallen_kortti
	kallen_kortti->>ratikka6: 3
	ratikka6->>kallen_kortti: vahenna_arvoa(1.5)
	kallen_kortti->>kallen_kortti: kallen_kortti.arvo = 1.5
	deactivate kallen_kortti
	ratikka6->>main: True
	deactivate deactivate

	main->>bussi244: osta_lippu(kallen_kortti, 2)
	activate bussi244
	bussi244->>kallen_kortti: arvo()
	activate kallen_kortti
	kallen_kortti->>bussi244: 1.5
	deactivate kallen_kortti
	bussi244->>main: False
	deactivate bussi244
