# **D&D Hex-grid maptool**

## Toiminta nyt - ja tulevaisuudessa

Suorittaessa komennon "poetry run invoke start" sovellus aukeaa ja pohjaksi määritellylle kuvalle piirtyy kuusikulmioverkosto, joka muodostuu kuusikulmio olioista. Ohjelma tunnistaa, mitä olentoa klikataan hiirellä. Ohjelman avaa sitä hexaolentoa vastaava tekstitiedoston geditissä, johoin voi kirjoittaa muistiinpanoja. 

Hiiren oikeata painiketta klikkaamalla ruudulle ilmestyy valikko, josta voi valita statblokkeja, joita lisätä hexaan. Tiedot näistä tallentuvat csv tiedostoon ja hexan statblockit tulevat näkyviin aina hexaa oikealla näppäimellä painettaessa.

### Ohjelman käynnistys

Ohjelma käynnistyy antamalla hex grid map kansiossa komento: "poetry run invoke start"

Testit komennolla "poetry run invoke test

Testikattavuusraportti komennolla "poetry run invoke coverage"

Pylint tarkistus komennolla "poetry run invoke lint"


### Dokumentaatio

[vaatimusmaarittely.md](https://github.com/kaariroo/ot-harjoitustyo/blob/master/hex-grid-app/dokumentaatio/vaatimusmaarittely.md)

[tyoaikakirjanpito.txt](https://github.com/kaariroo/ot-harjoitustyo/blob/master/hex-grid-app/dokumentaatio/tyoaikakirjanpito.txt)

[changelog.md](https://github.com/kaariroo/ot-harjoitustyo/blob/master/hex-grid-app/dokumentaatio/changelog.md)

[arkkitehtuuri.md](https://github.com/kaariroo/ot-harjoitustyo/blob/master/hex-grid-app/dokumentaatio/arkkitehtuuri.md)

[release](https://github.com/kaariroo/ot-harjoitustyo/releases)

[käyttöohje](https://github.com/kaariroo/ot-harjoitustyo/blob/master/hex-grid-app/dokumentaatio/kaytto-ohje.md)

Statblokkien kuvat ovat kuvakaappauksia dnd kirjasta "Monster Manual". Ohjelma ei ole julkiseen jakoon, vaan omaa käyttöä varten muistiinpanovälineenä ohjatessani dnd peliä.
