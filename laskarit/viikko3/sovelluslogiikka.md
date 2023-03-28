
```mermaid
classDiagram

	Pelilauta -- Ruutu
	Ruutu .. Pelinappula
	Pelaaja .. Noppa
	Noppa .. Pelinappula
	Pelaaja -- Pelinappula
	Pelilauta -- Pelinappula
	

	class Pelaaja{
		+Int id(1-8)
		+String nimi
		+heittaa(Noppax2)
		+siirtaa(Pelinappula, heittaa tulos)
	}
	
	class Pelilauta{
		+Int pelinappulat(2-8)
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
