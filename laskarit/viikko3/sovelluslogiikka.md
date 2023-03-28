
```mermaid
classDiagram

	Pelilauta -- Ruutu
	Ruutu .. Pelinappula
	Pelaaja .. Noppa
	Noppa .. Pelinappula
	Pelaaja -- Pelinappula
	

	class Pelaaja{
		+Int id
		+String nimi
		+heittaa(Noppa.tulos)
		+siirtaa(Pelinappula)
	}
	
	class Pelilauta{
		+List ruudut(40)

	class Ruutu{
		+Int id
		+String nimi
	}
	class Pelinappula{
		+Pelaaja.id omistaja
		+liikkuu()
	}
	class Noppa{
		+Int tulos
	}
