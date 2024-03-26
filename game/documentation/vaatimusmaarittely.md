# Vaatimusmäärittely
## Sovelluksen tarkoitus
Sovellus on kopio "Slay"-strategiapelistä. Peliä voi pelata 2-4 pelaajaa "hot-seat"-tyylisesti, eli kaikki pelaavat samalla laitteella. Pelikenttä muodostuu kuusikulmaisista ruuduista, joista jokainen kuuluu yhdelle pelaajista. Pelaajien on vuorollaan tarkoitus vallata itselleen mahdollisimman paljon alaa, mikä antaa pelaajalle lisää pisteitä. Pisteillä voi ostaa lisää sotilaita, joilla vallata uusia alueita. Pelin voittaa se pelaaja, joka valtaa koko pelikentän itselleen.

## Toiminnallisuus
Pelissä on:
* Pelikenttä, jonka ruudut on värikoodattu ruutua hallitsevan pelaajan mukaan. ✔️
* Sotilaita, jotka voivat vallata ruutuja sekä syödä toisiaan. Sotilailla on arvojärjestys, jossa nappulat voivat syödä vain pienempiään. Arvokkaammat sotilaat maksavat enemmän pisteitä. Sotilaita ylennetään viemällä kaksi sotilasta samaan ruutuun, jolloin tilalle syntyy arvokkaampi sotilas.
* Pisteitä, joilla palkataan uusia sotilaita. Pisteitä kertyy joka vuorolla sen mukaan, kuinka paljon alueita hallitsee. Sotilailla on ylläpitomaksu, joka vähennetään pistesaldosta joka kierroksella.
* Linnakkeita, joilla voi hidastaa muiden pelaajien etenemistä. Vain korkeamman arvon sotilaat voivat vallata ruutuja, joidenka lähellä on linnake.
* Alueita. Jokainen alue, jossa on useampi samanvärinen ruutu vierekkäin muodostaa oman alueensa, jolla on erillinen pistetalous muista saman pelaajan alueesta.

## Ohjaaminen
Pelissä on graafinen käyttöliittymä, jota ohjataan hiirellä.

## Jatkokehitysideoita

* Alkuperäisessä pelissä on myös puita, jotka kasvavat ja leviävät kuolleiden sotilaiden haudoilta. Ruudut, joissa on puita, eivät tuota pisteitä.
* Vaihtoehtoiset värit värisokeille pelaajille.
* Auditiivinen palaute.
* Yksinkertaisen tekoälyn kehittäminen tekisi sovelluksesta mielekkään yksinpelin.
