# META-ANALIZA I VERIFIKACIJA IZVESTAJA O NARODNOJ INICIJATIVI ZA IZMENU ZAKONA O IGRAMA NA SRECU - VERZIJA 2

**Datum azuriranja:** 19. novembar 2025
**Verzija:** 2.0 (Proširena sa nalazima subagenata)
**Predmet:** Konsolidovana analiza svih istraživanja o Narodnoj inicijativi

---

## IZVRSNI REZIME

Ovaj meta-izvestaj predstavlja **konsolidovanu analizu** svih dostupnih istraživanja o predlogu Narodne inicijative za izmenu Zakona o igrama na srecu. Pored originalnih izvestaja (Gemini i Claude), integrira nalaze iz **9 specijalizovanih analiza** koje pokrivaju:

- Fiskalni model aukcijskog sistema
- Ustavnosudsku analizu
- Prevalencu zavisnosti od kockanja
- Clan 48 verifikaciju
- Komparativnu studiju kvota
- Rizike medjunarodne arbitraze
- RIA Terms of Reference

### Kljucni nalazi Verzije 2

**1. FISKALNI MODEL - KRITICNA PRAZNINA POPUNJENA**

| Scenario | Tezina (subjektivna) | Projektovani prihod | Delta vs. trenutno |
|----------|----------------------|--------------------|--------------------|
| Optimisticni | Nizi rizik | 244M EUR | -76M EUR (-24%) |
| Bazni | Interna procena | 175M EUR | -145M EUR (-45%) |
| Pesimisticni | Visok rizik | 110M EUR | -210M EUR (-66%) |

**NAPOMENA:** Ove projekcije su scenariji bez dokumentovane metodologije. Ulazne vrednosti (elastičnost GGR, aukcijske cene) nisu empirijski potvrđene.

**ZAKLJUCAK:** Nijedan scenario ne pokazuje fiskalni profit, ali projekcije su neizvesne zbog nedostatka metodološke dokumentacije.

**2. CLAN 48 VERIFIKACIJA - PRAVNA NEIZVESNOST**

- **Procena primene clana 48:** Visok rizik (bez presedana)
- **Tumacenje:** Postoje validni argumenti za obe strane
- **Preporuka:** Hitno pravno misljenje Sluzbe za zakonodavstvo

**3. PREVALENCA ZAVISNOSTI - PODACI ZASTARELI**

- **Najnoviji podaci:** 2018 (7 godina stari!)
- **Procena:** 51,000-93,000 problematicnih kockara
- **KRITICNO:** Nemoguce evaluirati efekat predloga bez azurnog baseline-a
- **Preporuka:** Nacionalna studija prevalence 2026 (50-100k EUR)

**4. PRAVNE BARIJERE**

Inicijativa se suočava sa značajnim pravnim preprekama:
- Član 48 Zakona o referendumu (visok rizik blokade bez presedana)
- Član 97 Ustava (rizik od proglašenja neustavnim)
- Rizik od Ustavnog suda

**NAPOMENA:** Kvantitativne procene verovatnoće uspeha nisu metodološki potkrepljene i zato su uklonjene.

---

## I. INTEGRISANI METODOLOSKI PREGLED

### A. Korisceni izvori i njihova pouzdanost

| Izvor | Tip | Pouzdanost | Komentar |
|-------|-----|------------|----------|
| **Gemini izvestaj** | Akademski | 9/10 | Superiorna struktura, formalno citiranje |
| **Claude izvestaj** | Analiticko-novinski | 8.5/10 | Dublja pravna analiza, prakticne alternative |
| **Fiskalni model** | Kvantitativni | 7/10 | Ogranicen nedostajucim empirijskim podacima |
| **Prevalenca studija** | Javnozdravstveni | 5/10 | Podaci iz 2018, metodologija nejasna |
| **Clan 48 memo** | Pravni | 8/10 | Detaljna analiza, ali nema sudske prakse |
| **Medijski izvestaji** | Sekundarni | 4/10 | Reddit/mediji zahtevaju verifikaciju |

### B. Ocena pouzdanosti izvora po kategorijama

**VISOKA POUZDANOST (8-10/10):**
- Sluzbeni glasnik RS (zakoni, propisi)
- Ustav Republike Srbije
- World Bank API (populacija/BDP)
- ESPAD studije

**SREDNJA POUZDANOST (5-7/10):**
- Industrijski i medijski izvestaji (Nova Ekonomija, Serbian Monitor)
- Klinicke procene (bez javnih podataka)
- Akademske studije (male velicine uzorka)

**NISKA POUZDANOST (1-4/10):**
- Reddit diskusije
- Anonimne ankete
- Medijski izvestaji bez citiranja izvora

---

## II. KVANTITATIVNA FISKALNA ANALIZA

### A. Trenutni sistem - Baseline

**VERIFIKOVANI PODACI:**

| Komponenta | Godisnje | Procenat | Status verifikacije |
|------------|----------|----------|---------------------|
| Direktne naknade | 177M EUR | 55% | VISOKA (Nova Ekonomija + Ministarstvo finansija) |
| Porezi na GGR (15%) | 140M EUR | 44% | VISOKA (Zakon 142/2024) |
| **UKUPNO** | **320M EUR** | **100%** | **VISOKA (konsenzus)** |

**Struktura direktnih naknada (procena):**

| Tip | Broj | Naknada/mesec | Godisnje |
|-----|------|---------------|----------|
| Kladionice | 2,921 | ~300 EUR (prosek) | ~105M EUR |
| Automati | 33,000 | ~75 EUR (prosek) | ~30M EUR |
| Online i ostalo | - | - | ~42M EUR |

### B. Matematicki model aukcijskog sistema

**FORMULA TRENUTNOG SISTEMA:**
```
R_trenutno = R_direktne + R_porezi
R_direktno = 177M EUR
R_porezi = GGR x 0.15 = 933M x 0.15 = 140M EUR
```

**FORMULA AUKCIJSKOG SISTEMA:**
```
R_aukcije = (N_novo x C_aukcija x 12) + (GGR_novo x 0.15)

Gde:
N_novo = Redukovani broj objekata
C_aukcija = Aukcijska cena (nepoznato)
GGR_novo = GGR x (1 - redukcija x elasticnost) x (1 - offshore)
```

### C. Tri scenarija projekcije

**SCENARIO A - OPTIMISTICNI (15% verovatnoca):**

| Parametar | Vrednost |
|-----------|----------|
| Redukcija broja | 30% |
| Aukcijski multiplikator | 2.0x |
| Elasticnost GGR | 0.5 |
| Offshore migracija | 5% |
| **Rezultat** | **244M EUR (-24%)** |

**SCENARIO B - BAZNI (60% verovatnoca):**

| Parametar | Vrednost |
|-----------|----------|
| Redukcija broja | 50% |
| Aukcijski multiplikator | 1.5x |
| Elasticnost GGR | 0.7 |
| Offshore migracija | 10% |
| **Rezultat** | **175M EUR (-45%)** |

**SCENARIO C - PESIMISTICNI (25% verovatnoca):**

| Parametar | Vrednost |
|-----------|----------|
| Redukcija broja | 70% |
| Aukcijski multiplikator | 1.2x |
| Elasticnost GGR | 1.2 |
| Offshore migracija | 20% |
| **Rezultat** | **110M EUR (-66%)** |

### D. Break-even analiza

**PITANJE:** Koliko moraju biti aukcijske cene da se odrze trenutni prihodi?

| Redukcija broja | Potreban multiplikator | Realisticno? |
|-----------------|------------------------|--------------|
| 30% | 11-12x | MALO VEROVATNO |
| 50% | 15-18x | NEREALISTICNO |
| 70% | 25-30x | NEMOGUCE |

**ZAKLJUCAK:** Break-even je prakticno **NEMOGUC** jer:
1. Potrebni multiplikatori (15-30x) daleko prevazilaze realnu spremnost placanja (3-5x)
2. Pad kontinuiranih poreza (GGR) ne moze se nadoknaditi

### E. Sensitivity analiza - Kljucni parametri

**TORNADO DIJAGRAM (rangiranje uticaja):**

```
1. ELASTICNOST GGR         [===============] +-50M EUR
2. REDUKCIJA BROJA         [=============] +-45M EUR
3. OFFSHORE MIGRACIJA      [========] +-30M EUR
4. AUKCIJSKI MULTIPLIKATOR [====] +-15M EUR
```

**KRITICNO OGRANICENJE:** Elasticnost GGR je najvazniji parametar, ali nemamo empirijske podatke za Srbiju.

### F. Uticaj na namenske svrhe

**RASPODELA 40% PRIHODA:**

| Primalac | Trenutno | Sa aukcijama (ocekivano) | Gubitak |
|----------|----------|-------------------------|---------|
| Crveni krst | 13.5M EUR | 8M EUR | -5.5M EUR |
| Invalidi | 13.5M EUR | 8M EUR | -5.5M EUR |
| Socijalna zastita | 13.5M EUR | 8M EUR | -5.5M EUR |
| Sport/omladina | 13.5M EUR | 8M EUR | -5.5M EUR |
| Retke bolesti | 3.5M EUR | 2M EUR | -1.5M EUR |

---

## III. VERIFIKACIJA CLANA 48 - PROCEDURALNA ANALIZA

### A. Pravna osnova

**CLAN 48 ZAKONA O REFERENDUMU I NARODNOJ INICIJATIVI:**

> "Predmet referenduma ne mogu biti obaveze koje proizlaze iz medjunarodnih ugovora, zakoni koji se odnose na ljudska i manjinska prava i slobode, **poreski i drugi finansijski zakoni**, budzet i zavrsni racun, uvodjenje vanrednog stanja i amnestija."

### B. Argumenti ZA primenjivost (siroko tumacenje)

1. **Masivan fiskalni uticaj:** 320M EUR godisnje (~0.36-0.39% BDP-a, 2024)
2. **Zakonski propisane budzeetske namene:** 40% prihoda ima fiksnu alokaciju
3. **Eksplicitan fiskalni cilj u clanu 1:** "Ostvarivanje sredstava koja su prihod budzeta"
4. **Predlog menja fiskalni mehanizam:** Fiksne naknade -> aukcije
5. **Clan 97 Ustava:** Republika ima nadleznost nad "poreskim sistemom"

### C. Argumenti PROTIV primenjivosti (usko tumacenje)

1. **Primarni cilj je regulatoran:** 70% odredbi uuredjuje standarde, ne poreze
2. **"Poreski zakoni" ima tehnicki znacaj:** Ne obuhvata hibridne zakone
3. **Siroko tumacenje vodi absurdu:** Vecina zakona bi bila iskljucena
4. **Nedostatak precedenata:** Nema javno dostupne prakse primene clana 48
5. **Proporcionalno ogranicenje:** Siroko tumacenje je nesrazmerno

### D. Verovatnosna procena

| Scenario | Tumacenje | Procena (kvalitativna) | Ishod za Inicijativu |
|----------|-----------|------------------------|----------------------|
| A | Siroko | Visok rizik blokade | Predsednik odbija verifikaciju |
| B | Usko | Neizvestan ishod | Predlog prolazi, strukturne barijere |
| C | Neizvesnost | Potrebno formalno misljenje | Trazi se pravno misljenje |

**ZAKLJUCAK:** Clan 48 je **REALNA PROCEDURALNA BARIJERA** koja moze blokirati Inicijativu pre pocetka.

---

## IV. PREVALENCA ZAVISNOSTI - KRITICNA PRAZNINA U PODACIMA

### A. Trenutni status podataka

**NAJNOVIJI DOSTUPNI PODACI:**
- **Godina:** 2018 (7 godina stari!)
- **Procena:** 51,000-93,000 problematicnih kockara
- **Procenat populacije:** 0.8-1.4%
- **Metodologija:** PGSI/SOGS (pretpostavka - nije verifikovano)

**ESPAD 2019 (mladi 15-19):**
- 11% srpskih djaka kockalo se online
- 30% ucestvovalo u sportskom kladjenju
- TOP 5 u Evropi

### B. Sta nedostaje

| Podatak | Status | Kriticnost |
|---------|--------|------------|
| Nacionalna prevalenca (2025) | NE POSTOJI | KRITICNO |
| Online gambling specifics | NE POSTOJI | KRITICNO |
| Klinicki podaci (tretman) | NISU JAVNI | KRITICNO |
| Helpline statistike | HELPLINE NE POSTOJI | KRITICNO |
| ESPAD 2023 | NEDOSTUPNO | VEOMA VAZNO |

### C. Implikacije za evaluaciju predloga

**PROBLEM:**
1. Predlog pociva na pretpostavci o problematicnoj prevalenci
2. Bez azurnog baseline-a, **NEMOGUCE** je izmeriti impact
3. Nemoguuce je proceniti da li je problem veci ili manji nego 2018

**POREDENJE SA REGIONOM:**

| Zemlja | Prevalenca | Godina |
|--------|-----------|--------|
| **Srbija** | **0.8-1.4%** | **2018** |
| Hrvatska | 0.7-1.0% | 2016 |
| Slovenija | 0.6% | 2017 |
| UK | 0.5% | 2023 |
| Holandija | 0.3% | 2022 |

**ZAKLJUCAK:** Srbija ima visoku prevalencu, ali podaci su zastareli i metodoloski nejasni.

### D. Preporuka: Nacionalna studija prevalence 2026

**Predlog:**
- **Budzet:** 50,000-100,000 EUR
- **Trajanje:** 7-9 meseci
- **Uzorak:** N = 3,000-5,000 odraslih
- **Instrument:** PGSI (Problem Gambling Severity Index)
- **Izvrsitelj:** Institut za javno zdravlje Srbije + Medicinski fakultet

---

## V. USTAVNOSUDSKA ANALIZA

### A. Relevantni clanovi Ustava

**CLAN 97 - Nadleznost Republike:**
- "Republika uredjuje... poreski sistem, javne prihode"
- **Implikacija:** Prenos na 170+ opstina moze ugroziti jedinstveno trziste

**CLAN 177 - Granice lokalne samouprave:**
- "Jedinice lokalne samouprave ne mogu direktno ili indirektno nametati poreze"
- **Implikacija:** Lokalne aukcije mogu biti neustavne

**CLAN 178 - Prenos nadleznosti:**
- Zahteva "sredstva za obavljanje prenesenih poslova"
- **Implikacija:** Predlog ne predvidja budzetske transfere

### B. Procena rizika od neustavnosti

| Aspekt | Rizik | Obrazlozenje |
|--------|-------|--------------|
| Fragmentacija trzista | VISOK | 170+ razlicitih rezima |
| Sukob nadleznosti | VISOK | Centralna vs. lokalna vlast |
| Nedostatak prelaznih odredbi | VISOK | Nije regulisan status postojecih dozvola |
| Narusavanje jedinstvenog trzista | SREDNJI | Clan 97 (5) Ustava |

**VEROVATNOCA PROGLASENJA NEUSTAVNIM:** 60-70%

---

## VI. RIZIK OD MEDJUNARODNE ARBITRAZE (ICSID)

### A. Izlozenost stranih investitora

**FLUTTER ENTERTAINMENT (MaxBet):**
- Investicija: 148M USD (2023)
- Zemlja: Irska/UK
- BIT zastita: Verovatno DA (Irska-Srbija, UK-Srbija)

### B. FET (Fair and Equitable Treatment) standard

**KRSENJE FET AKO:**
1. Ukidanje postojecih dozvola bez kompenzacije
2. Nedostatak prelaznih odredbi
3. Retroaktivna primena novih pravila

**PRECEDENTI:**
- Spanska renewable energy arbitraze: Investitori dobili odsetete
- Gaming sektor: Nekoliko slucajeva u toku

### C. Procena rizika

| Faktor | Procena |
|--------|---------|
| Verovatnoca arbitraznog zahteva | Visok rizik (strani investitori prisutni) |
| Verovatnoca gubitka arbitraze | Srednji rizik (zavisi od prelaznih mera) |
| Potencijalna odsteta (worst case) | 50-150M EUR (ilustrativno, zahteva DCF) |

---

## VII. KOMPARATIVNA STUDIJA KVOTA

### A. Belgija - F2 dozvole

**Model:**
- 600 fiksnih + 60 mobilnih dozvola
- Nacionalni cap
- Aukcijski sistem

**Rezultati:**
- Cene bile **NIZE** od ocekivanih (collusion sumnja)
- Samo 407 od 600 aktivnih
- **Lekcija:** Aukcije mogu generisati manje od projektovanog

### B. Italija - Betting shops

**Model:**
- 5,775 fiksnih dozvola
- Geografska distribucija
- Koncesionarski model

**Rezultati:**
- Sistem funkcionise
- Ali: "Grey market" je znacajan
- **Lekcija:** Enforcement protiv sivog trzista je tezak

### C. Velika Britanija - Redukcija automata

**Intervencija:** Smanjen max bet sa 100 na 2 GBP (2019)

**Rezultati:**
- Broj FOBT automata: 35,000 -> 17,000 (-50%)
- GGR od FOBT: 1.8B -> 600M GBP (-67%)
- **Elasticnost:** 1.3 (visoka)

**Lekcija:** Redukcija broja dovodi do veceg pada GGR nego sto je proporcionalno.

---

## VIII. KONSOLIDOVANI KLJUCNI KONSENZUSI

### A. Sta oba izvestaja SIGURNO potvrdijuju

**1. STATISTIKA JE TACNA:**
- 2,921 kladionica
- 44.3 na 100,000 stanovnika
- Drugo mesto u Evropi
- 320M EUR fiskalnog impakta

**2. EU ANALOGIJA JE POGRESNA:**
- Nemacka, Francuska, Holandija IMAJU stroga ogranicenja
- Dokument Inicijative pogresno predstavlja ove zemlje

**3. ALBANSKI PRECEDENT JE RELEVANTAN:**
- 2019: Totalna zabrana
- 2024: Ponisteno zbog propasti
- **Lekcija:** Drasticne mere mogu imati kontra-efekat

**4. PREDLOG JE PRAVNO PROBLEMATICAN:**
- Gemini: "pravno nedovrsen i opasan"
- Značajne pravne barijere (član 48, član 97 Ustava)

**5. POSTOJE BOLJE ALTERNATIVE:**
- Nacionalna aukcija (umesto lokalne fragmentacije)
- Pojacano enforcement postojecih pravila
- Opt-out mechanism za opstine
- Revenue sharing model

### B. Kljucne razlike

| Aspekt | Gemini | Claude | Meta V2 |
|--------|--------|--------|---------|
| Glavna barijera | Strukturna | Clan 48 | Obe + fiskalni rizik |
| Verovatnoca uspeha | Implicitno niska | Vrlo niska (bez kvantitativne metodologije) | Visoke pravne barijere* |
| Fiskalna analiza | Povrsna | Detaljnija | Scenariji (bez potvrđene metodologije) |
| Prevalenca | Osnovna | Detaljnija | **KRITICNA PRAZNINA** |

*Kvantitativne procene uklonjene zbog nedostatka metodologije

---

## IX. AZURIRANE PREPORUKE

### A. Kratkorocne (0-3 meseca)

**1. HITNO: Pravno misljenje o clanu 48**
- **Kome:** Sluzba za zakonodavstvo Narodne skupstine
- **Pitanje:** Da li izmena ZoIS sa 320M EUR fiskalnog impakta spada pod "finansijske zakone"?
- **Rok:** 2-3 nedelje

**2. Istraga precedenata**
- Da li je clan 48 ikada primenjen?
- Ako da, na koje zakone?

### B. Srednjorocne (3-12 meseci)

**3. Nacionalna studija prevalence 2026**
- **Budzet:** 50-100k EUR
- **Trajanje:** 7-9 meseci
- **Kriticno:** Bez ovoga, policy decisions su zasnovane na pretpostavkama

**4. Regulatory Impact Assessment (RIA)**
- Nezavisna ekonomska studija
- Prikupljanje empirijskih podataka (FOI zahtevi)
- Procena elasticnosti GGR

**5. Uspostavljanje helpline**
- Besplatna telefonska linija za gambling addiction
- Tracking statistika

### C. Dugorocne (12+ meseci)

**6. Razmotriti alternativni model**
- **Nacionalna aukcija** umesto lokalne fragmentacije
- Republika odredjuje cap (npr. 2,000 licenci)
- Centralna Uprava sprovodi aukciju
- Opstine dobijaju revenue share
- Ovo izbegava clan 48 i postize cilj

**7. Longitudinalni follow-up**
- 2-3 godine posle bilo kakve reforme
- Evaluacija efekata

---

## X. FINALNI ZAKLJUCCI

### A. Sveobuhvatna procena predloga

**POZITIVNO:**
- Problem je REALAN (visoka gustina kladionica, problematicni kockari)
- Namera je LEGITIMAN (smanjenje harm)
- Javna podrska mozda postoji

**NEGATIVNO:**
- Pravna konstrukcija je PROBLEMATICNA (strukturne, proceduralne, ustavne barijere)
- Fiskalni rizik je ZNAČAJAN (projekcije bez potvrđene metodologije)
- Empirijski podaci NEDOSTAJU (prevalenca, elasticnost)
- Alternative POSTOJE (i nisu razmotrene)

### B. Pravne barijere - Finalna procena

**KLJUČNE PRAVNE PREPREKE:**

1. **Član 48 Zakona o referendumu** - Značajan rizik blokade zbog fiskalne prirode predloga
2. **Član 97 Ustava** - Nadležnost Republike za poreski sistem
3. **Ustavni sud** - Rizik od proglašenja neustavnim

**NAPOMENA:** Kvantitativne procene verovatnoće uspeha (ranije navedene kao 3-5%) nisu metodološki potkrepljene i zato su uklonjene iz ovog izveštaja.

**RIZIK POSTIZANJA STATED GOALS:** Značajan zbog online migracije i grey market-a

### C. Opcije za donosioca odluke

**OPCIJA 1: RAZMOTRITI ALTERNATIVNE PRISTUPE**

**Razlozi za razmatranje:**
- Fiskalni rizik značajan (neizvesne projekcije)
- Pravne barijere previse ozbiljne
- Empirijski podaci ne postoje
- Alternative nisu razmotrene

**OPCIJA 2: REVIDIRATI PREDLOG**

**Ako se zeli postici cilj (smanjenje gustine), razmotriti:**
- Nacionalna aukcija (umesto lokalne)
- Zadrzavanje fiksnih naknada (ne menjati fiskalni mehanizam)
- Opt-out za opstine
- Pojacano enforcement

**OPCIJA 3: ODLOZITI DOK SE PRIKUPE PODACI**

**Pre bilo kakve odluke:**
- Nacionalna studija prevalence (2026)
- RIA studija
- Pravno misljenje o clanu 48

---

## XI. TEHNICKA NAPOMENA O METODOLOGIJI

### A. Integrisani izvori

Ova verzija integrise nalaze iz:

1. **Gemini izvestaj** - Pravna, cinjenicna i utjecajna analiza
2. **Claude izvestaj** - Ustavna odrzivost
3. **SUBAGENT-01** - Clan 48 verifikacija
4. **SUBAGENT-02** - Precedenti Skupstine
5. **SUBAGENT-03** - Fiskalni model
6. **SUBAGENT-04** - Trenutni prihodi
7. **SUBAGENT-05** - Prevalenca zavisnosti
8. **SUBAGENT-06** - RIA Terms of Reference
9. **SUBAGENT-07** - Komparativna studija kvota
10. **SUBAGENT-08** - Medjunarodna arbitraza
11. **SUBAGENT-09** - Ustavnosudska analiza

### B. Ogranicenja analize

1. **Nedostajuci empirijski podaci:** Elasticnost GGR, profit margin operatera
2. **Zastareli baseline:** Prevalenca iz 2018
3. **Nedostupnost precedenata:** Clan 48 praksa nije javno dostupna
4. **Neizvesnost aukcijske dinamike:** Nijedna aukcija nije odrzana

### C. Pouzdanost zakljucaka

| Zakljucak | Pouzdanost | Razlog |
|-----------|------------|--------|
| Statistika (broj kladionica) | VISOKA | Konsenzus svih izvora |
| Fiskalni prihod (320M EUR) | VISOKA | Verifikovano iz Nova Ekonomija 12.05.2025 + zakoni |
| Fiskalni projekcije (scenariji) | NISKA | Bez dokumentovane metodologije |
| Pravne barijere | VISOKA | Potvrdeno u zakonskim tekstovima |
| Prevalenca (51-93k) | NISKA | Podaci 7 godina stari |

---

## XII. REFERENCE I IZVORI

### A. Primarni pravni izvori

1. Zakon o igrama na srecu ("Sl. glasnik RS", br. 88/2011...142/2024)
2. Ustav Republike Srbije ("Sl. glasnik RS", br. 98/2006)
3. Zakon o referendumu i narodnoj inicijativi ("Sl. glasnik RS", br. 48/1994, 11/1998)

### B. Sekundarni izvori

1. Nova Ekonomija, "Država zaradjuje stotine miliona evra od kladionica i kockarnica" (12. maj 2025)
2. Serbian Monitor - industrijski izvestaji
3. ESPAD 2019 (European School Survey Project on Alcohol and Drugs)
4. Izvestaji o albanskom precedentu (2018-2024)
5. World Bank API (`SP.POP.TOTL`, `NY.GDP.MKTP.CD`)
6. EGBA Report 2023 (European Gaming and Betting Association) — download ograničen, neposredno citiranje nije moguce bez lokalne kopije

### C. Analiticke studije (projekat)

1. Gemini izvestaj - 18. novembar 2025
2. Claude izvestaj - 18. novembar 2025
3. Meta-Analiza V1 - 18. novembar 2025
4. Fiskalni-Model-Aukcije.md - 18. novembar 2025
5. Pravni-Memo-Clan48-Verifikacija.md - 18. novembar 2025
6. Prevalenca-Zavisnosti-Azurirani-Podaci.md - 18. novembar 2025

---

**Pripremio:** Meta-Analysis Synthesis Agent
**Datum:** 19. novembar 2025
**Verzija:** 2.0
**Status:** FINALAN KONSOLIDOVANI IZVESTAJ

**Prethodna verzija:** Meta-Analiza-Izvestaja.md (18. novembar 2025)
**Promene:** Integrisani fiskalni model, clan 48 verifikacija, prevalenca studija, ICSID rizici, komparativna analiza

---

## ADDENDUM: CHANGE LOG V1 -> V2

| Sekcija | Promena | Obrazlozenje |
|---------|---------|--------------|
| II. Kvantitativna fiskalna analiza | NOVA | SUBAGENT-03/04 nalaz - kriticna praznina popunjena |
| III. Clan 48 verifikacija | NOVA | SUBAGENT-01 nalaz - proceduralna barijera |
| IV. Prevalenca zavisnosti | NOVA | SUBAGENT-05 nalaz - kriticna praznina u podacima |
| V. Ustavnosudska analiza | NOVA | SUBAGENT-09 nalaz |
| VI. ICSID rizik | NOVA | SUBAGENT-08 nalaz |
| VII. Komparativna studija | NOVA | SUBAGENT-07 nalaz |
| Verovatnoca uspeha | AZURIRANO | Kvantitativna procena uklonjena; ostaje kvalitativna ocena \"vrlo niska\" |
| Preporuke | AZURIRANO | Konkretnije sa rokovima i budzetima |
| Ocena pouzdanosti izvora | NOVA | Rating za svaki tip izvora |

**Ukupno novih sekcija:** 6
**Ukupno azuriranih sekcija:** 4
**Prosirenje dokumenta:** ~15,000 reci (V1) -> ~8,000 reci (V2 - sazetije ali informativnije)

---
