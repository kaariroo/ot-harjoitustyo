
```mermaid
classDiagram

	Pelilauta -- Ruutu
	Ruutu .. Pelinappula
	Pelaaja .. Noppa
	Noppa .. Pelinappula
	Pelaaja -- Pelinappula
	Pelilauta -- Pelinappula
	Ruutu <|-- Aloitusruutu
	Ruutu <|-- Vankila
	Ruutu <|-- Sat_ja_yht
	Sat_ja_yht -- Kortti
	Ruutu <|-- Normikatu
	Normikatu .. Pelaaja
	Ruutu <|-- Asematjalaitokset

	class Asematjalaitokset{
		+Int id
		+String nimi
		+String omistaja
	}

	class Normikatu{
		+Int id
		+String nimi
		+String omistaja
		+rakennatalo(1-4)
		+rakennahotelli(puratalot, hotelli)
	}
	class Kortti{
		+Int id
		+toiminto(id)
	}

	class Sat_ja_yht{
		+Int id
		+nosta_kortti(kortti)
	}
	
	class Aloitusruutu{
		+Id 1
		+Aloitus
		+nosto(4000mk)
	}

	class Vankila{
		+Id 30
		+Vankila
		+jumissa(heittaa parin)

	class Pelaaja{
		+Int id(1-8)
		+Int rahamäärä
		+String nimi
		+heittaa(Noppax2)
		+siirtaa(Pelinappula, heittaa tulos)
	}
	
	class Pelilauta{
		+Int pelinappulat(2-8)
		+List ruudut(40)
	}
	class Ruutu{
		+Int id(1-40)
		+String nimi
		+Int oikea ruutu id-1
		+Int vasen ruutu id+1
	}
	class Pelinappula{
		+Pelaaja.id omistaja
		+liikkuu()
	}
	class Noppa{
		+Int tulos
	}
