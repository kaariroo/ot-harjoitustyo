# Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/kaariroo/ot-harjoitustyo/releases/tag/viikko_5) lähdekoodi valitsemalla _Assets_-osion alta _Source code_.

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

```bash
poetry install
```

Nyt ohjelman voi käynnistää komennolla:

```bash
poetry run invoke start
```
## Ohjelman käyttäminen

Hiiren vasemmalla painikkeella karttaa painettaessa aukeaa klikattua hexaa
vastaava tekstitiedosto. sinne voi kirjoittaa muistiinpanoja kartan siitä
hexasta. Tallenna muistiinpano "save" nappulalla.

Hiiren oikealla painikkeella painettaessa aukeaa oikealle ylös valikko, josta voi valita, mitä statblokkeja
hexaan haluaa. Kun valikosta klikkaa hiiren vasemmalla painikkeella, ilmestyy kyseinen statblokki ikkunaan ja 
tallentuu csv tiedostoon. Valikko ja statblokit sulkeutuvat klikkaamalla samaa hexaa uudestaan oikealla painikkeella
tai valikon otsikkoa "monsters" hiiren vasemmalla painikkeella.

