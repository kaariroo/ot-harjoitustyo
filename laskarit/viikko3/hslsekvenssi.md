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
	lippu_luukku activate
	lippu_luukku->>kallen_kortti: Matkakortti("Kalle")
	lippu_luukku deactivate
	
	main->>rautatietori: lataa_arvoa(kallen_kortti, 3)
	rautatietori activate
	rautatietori->>kallen_kortti: kasvata_arvoa(3)
	rautatietori deactivate
	kallen_kortti activate
	kallen_kortti->>kallen_kortti: kallen_kortti.arvo = 3
	kallen_kortti deactivate

	main->>ratikka6: osta_lippu(kallen_kortti, 0)
	ratikka6 activate
	ratikka6->>kallen_kortti: arvo()
	kallen_kortti activate
	kallen_kortti->>ratikka6: 3
	ratikka6->>kallen_kortti: vahenna_arvoa(1.5)
	kallen_kortti->>kallen_kortti: kallen_kortti.arvo = 1.5
	kallen_kortti deactivate
	ratikka6->>main: True
	ratikka6 deactivate

	main->>bussi244: osta_lippu(kallen_kortti, 2)
	bussi244 activate
	bussi244->>kallen_kortti: arvo()
	kallen_kortti activate
	kallen_kortti->>bussi244: 1.5
	kallen_kortti deactivate
	bussi244->>main: False
	bussi244 deactivate
