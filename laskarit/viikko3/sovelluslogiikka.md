
```mermaid
classDiagram

	Pelilauta -- Ruutu
	Ruutu -- Peilnappula
	Pelaaja .. Noppa
	Noppa .. Pelinappula
	Pelaaja -- Pelinappula
	

	class Pelaaja{
		+Int id
		+String nimi
		+heittaa(Noppa)
		+siirtaa(Pelinappula)
	}
	
	class Pelilauta

	class Ruutu{
		+Int id
		+String nimi
	}
	class Pelinappula{
		+Pelaaja.id omistaja
	}
	class Noppa
		+
