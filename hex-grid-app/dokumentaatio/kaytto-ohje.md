#Käyttöohje

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

Hiiren oikealla painikkeella painettaessa aukeaa suden statblokki. 
Tavoitteena on että jokaiselle hexalle voisi määritellä mitä statblokkeja
niihin aukeaa ja ne esim. suurentuisivat kun hiiren vie niiden päälle, mikä 
helpottaisi lukemista ja ne saisi tietty suljettuakin.
