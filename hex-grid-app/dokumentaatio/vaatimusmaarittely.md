# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksella käyttäjä luo haluamansa kartan päälle hex-grid ruudukon kuusikulmioista, joita klikkaamalla aukeaa muistiinpanotyöväline johon on mahdollista tehdä muistiinpanoja siitä mitä kartalla 
kyseisessä hexassa on. Sovelluksen päätarkoitus on toimia muistiinpanovälineenä Dungeons & Dragons peliä varten piirretyn kartan sisällöstä. Muistiinpanoja pitää pystyä muuttamaan sitä mukaan kun 
peliä pelatessa kartan maailmaan tapahtuu muutoksia. Myös uudelleen piirretyn samankokoisen kartan lisääminen vanhan hexan päälle(tai oikeastaan alle) olisi oleellinen ominaisuus jos itse pohjana 
olevaan karttaan haluaakin tehdä muutoksia.

## Käyttäjät

Sovelluksella on alkuun vain yksi käyttäjärooli eli _normaali käyttäjä_. 

## Käyttöliittymäideoinita

Sovelluksen auetessa käyttäjälle aukeaa ikkuna jossa on mahdollista ladata aiempi kartta, tai aloittaa uuden luominen. Uutta luomaan ryhtyessa aukeaa painike, josta voi ladata sovellukseen kuvan, 
(joka tulee ns. "kartaksi" pohjalle) ja määrittää hexojen määrän kartan päällä. Tämän jälkeen siirrytään näkymään, jossa voi tehdä muutoksia ruudukkoon ja muistiinpanoja.

## Toiminnallisuus

### Alkunäkymä

Sovelluksen auetessa ilmestyvässä ikkunassa on naviskat "uusi kartta" ja "vanha kartta". Valitessa vanhan voi ladata vanhan projektin, jota muokata ja tutkia. Uuden valitessa ladataan koneelta kuva,
joka tulee kartan pohjaksi. Tämän jälkeen tulee ruutu, johon syötetään "hex gridin" korkeus ja leveys hexoissa ja sovellus luo ruudukon kuvan päälle.

### Muokkausnäkymä

Täällä voi muokata projektia joko klikkaamalla hexaa(TEHTY), jolloin pääsee kirjoittamaan siitä hexasta muistiinpanoja, tai liikuttamalla hexaruudukkoa kuvan päällä (jos tarvetta saada hexat johonkin 
tiettyihin kohtiin.

### Jatkokehitysideoita

Jossain vaiheessa haluan mahdollisuuden vaihtaa hexakon alla olevan kartan uuteen, niin että hexojen tiedot säilyvät. Ties vaikka kartan maailmaa järisyttää jokin luononmullistus ja puolet kartasta
uppoaa mereen.
