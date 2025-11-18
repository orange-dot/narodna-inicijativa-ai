# PLAN IZVRŠENJA: SUBAGENTI ZA UNAPREĐENJE ANALIZA

**Datum:** 18. novembar 2025
**Baziran na:** Cross-Check-Sinteza-Final.md
**Status:** Plan za izvršenje

---

## OVERVIEW: Struktura subagenata

Ovaj dokument definiše **15 konkretnih subagenata** za izvršenje svih unapređenja identifikovanih u cross-check analizi.

### Klasifikacija po prioritetu:
- 🔴 **PRIORITET 1 (KRITIČNI):** 5 subagenata - Pre bilo kakve dalje odluke
- 🟠 **PRIORITET 2 (VEOMA VAŽNI):** 4 subagenta - Ako predlog prođe član 48 test
- 🟡 **PRIORITET 3 (VAŽNI):** 6 subagenata - Dugoročna unapređenja

### Klasifikacija po tipu:
- **Pravni:** 4 subagenta
- **Ekonomski/Fiskalni:** 3 subagenta
- **Istraživački:** 3 subagenta
- **Dokumentacioni:** 5 subagenata

---

## 🔴 PRIORITET 1: KRITIČNI SUBAGENTI

### SUBAGENT-01: Pravna Verifikacija Člana 48

**Tip:** Pravni istraživački
**Prioritet:** 🔴 KRITIČAN
**Trajanje:** 1-2 dana (za AI istraživanje)
**Odgovoran:** AI Legal Research Agent

#### Zadatak:
Detaljno istražiti i dokumentovati primenjivost člana 48 Zakona o referendumu i narodnoj inicijativi na predlog izmene Zakona o igrame na sreću.

#### Deliverables:
1. **Pravni memo** (3-5 strana) koji sadrži:
   - Tačan tekst člana 48 Zakona
   - Analiza pojma "finansijski zakoni"
   - Uporedna analiza sa drugim jurisdikcijama
   - Argumenti ZA i PROTIV primenjivosti
   - Finalna pravna ocena

2. **Tabela precedenata** ako postoje

#### Potrebni resursi:
- Zakon o referendumu i narodnoj inicijativi (Paragraf.rs)
- Ustav Republike Srbije
- Relevantna sudska praksa
- Stručna literatura o referendumu

#### Istraživačka pitanja:
1. Da li se "finansijski zakoni" odnose SAMO na direktne poreze ili i na zakone sa fiskalnim implikacijama?
2. Da li je član 48 ranije primenjivan u praksi Narodne skupštine?
3. Kako su slični slučajevi rešavani u drugim zemljama?

#### Output fajl:
`Pravni-Memo-Clan48-Verifikacija.md`

---

### SUBAGENT-02: Pregled Precedenata Narodne Skupštine

**Tip:** Istraživački (arhivski)
**Prioritet:** 🔴 KRITIČAN
**Trajanje:** 2-3 dana
**Odgovoran:** AI Archive Research Agent

#### Zadatak:
Pronaći SVE slučajeve u istoriji Narodne skupštine gde je član 48 Zakona o referendumu bio razmatran, primenjen ili sporan.

#### Deliverables:
1. **Baza precedenata** (tabela) sa:
   - Datum i naziv inicijative
   - Da li je član 48 primenjen?
   - Obrazloženje odluke
   - Ishod (odbijeno/prihvaćeno)

2. **Analitički izveštaj** (5-7 strana):
   - Identifikacija obrazaca u primeni člana 48
   - Da li postoji konzistentna praksa?
   - Implikacije za trenutnu inicijativu

#### Potrebni resursi:
- Arhiva Narodne skupštine
- Stenogrami sednica
- Odluke Predsednika Skupštine
- Službeni glasnik

#### Istraživačka pitanja:
1. Koliko puta je član 48 bio osnov za odbijanje verifikacije?
2. Da li je neka inicijativa sa fiskalnim implikacijama prošla verifikaciju?
3. Koja je tipična argumentacija za primenu/neprimenu člana 48?

#### Output fajl:
`Precedenti-Clan48-Analiza.md`

---

### SUBAGENT-03: Kvantitativna Fiskalna Analiza (Matematički Model)

**Tip:** Ekonomski/Fiskalni
**Prioritet:** 🔴 KRITIČAN
**Trajanje:** 3-5 dana
**Odgovoran:** AI Financial Modeling Agent

#### Zadatak:
Kreirati **precizni matematički model** koji kvantifikuje fiskalne efekte trenutnog sistema vs. predloženog sistema aukcija.

#### Deliverables:
1. **Excel/Google Sheets model** sa:
   - Trenutni prihodi (po tipu naknade)
   - Projekcije aukcijskih prihoda (3 scenarija)
   - Break-even analiza
   - Osetljivost na parametre

2. **Izveštaj** (10-15 strana) koji sadrži:
   - Metodologija i pretpostavke
   - Best/Base/Worst case scenariji
   - Vizualizacije (grafikoni, tabele)
   - Rizici i neizvesnosti
   - Preporuke

#### Potrebni podaci (za istraživanje):
1. **Trenutni sistem:**
   - Koliko država TRENUTNO zarađuje na naknadama po kladionici/automatu?
   - Koliko je minimalna naknad po članu 75 i 90 ZoIS?
   - Koliko operatera plaća IZNAD minimuma?

2. **Projekcije aukcija:**
   - Koliko bi operateri bili spremni da plate?
   - Koliki je profit po kladionici/automatu?
   - Kolika je elastičnost tražnje?

#### Model scenariji:

**SCENARIO A: Optimistični (blaga redukcija, visoka cena)**
```
Pretpostavke:
- Redukcija broja: 30% (2,921 → 2,045 kladionica)
- Prosečna aukcijska cena: +100% vs. trenutne naknade
- Kontinuirani porezi (15% GGR): bez promene

Kalkulacija:
[TRENUTNO]
- Kladionice: 2,921 × X€/mesec × 12 = Y€/god
- Automati: 33,000 × Z€/mesec × 12 = W€/god
UKUPNO naknade: ?€

[SA AUKCIJOM]
- Kladionice: 2,045 × (2X)€/mesec × 12 = ?€/god
- Automati: 23,100 × (2Z)€/mesec × 12 = ?€/god
UKUPNO: ?€

Delta: ?%
```

**SCENARIO B: Bazni (umerna redukcija, umerena cena)**
```
- Redukcija: 50%
- Cena: +50%
Delta: ?%
```

**SCENARIO C: Pesimistični (drastična redukcija, visoka cena)**
```
- Redukcija: 70%
- Cena: +200%
Delta: ?%
```

#### Potrebni resursi:
- Zakon o igrama na sreću (članovi 75, 90 - trenutne naknade)
- Finansijski izveštaji Uprave za igre na sreću
- Finansijski podaci operatera (ako javno dostupni)
- Uporedni podaci iz Belgije/Italije

#### Output fajlovi:
1. `Fiskalni-Model-Aukcije.xlsx` (ili Google Sheets link)
2. `Fiskalna-Analiza-Izvestaj.md`

---

### SUBAGENT-04: Istraživanje Trenutnih Prihoda od Naknada

**Tip:** Istraživački (podatkovni)
**Prioritet:** 🔴 KRITIČAN
**Trajanje:** 2-3 dana
**Odgovoran:** AI Data Research Agent

#### Zadatak:
Pronaći TAČNE podatke o trenutnim prihodima od naknada za kladionice i automate (koliko država TRENUTNO zarađuje od sistema fiksnih naknada).

#### Deliverables:
1. **Tabela prihoda** sa:
   - Prihod od naknada po kladionicama (godišnje)
   - Prihod od naknada po automatima (godišnje)
   - Prihod od kontinuiranih poreza (15% GGR)
   - UKUPNO fiskalni prihod
   - Podela po namenama (40% za Crveni krst, sport, etc.)

2. **Metodološka napomena**:
   - Izvor podataka
   - Stepen pouzdanosti
   - Ograničenja podataka

#### Potrebni resursi:
- Uprava za igre na sreću (godišnji izveštaji)
- Ministarstvo finansija (budžetski izveštaji)
- Zakon o igrama na sreću (članovi 75, 90)
- Službeni glasnik
- FOI (Freedom of Information) zahtev ako potrebno

#### Istraživačka pitanja:
1. Koliki je iznos minimalne naknade po članu 75 (automati) i 90 (kladionice)?
2. Koliko operatera plaća više od minimuma?
3. Kako se prihodi distribuiraju (Republika vs. opštine)?
4. Koliki je prihod od poreza na GGR (15%)?

#### Output fajl:
`Trenutni-Fiskalni-Prihodi-Podaci.md`

---

### SUBAGENT-05: Ažuriranje Podataka o Problematičnim Kockarima

**Tip:** Istraživački
**Prioritet:** 🔴 KRITIČAN
**Trajanje:** 2-3 dana
**Odgovoran:** AI Public Health Research Agent

#### Zadatak:
Pronaći najnovije dostupne podatke o broju problematičnih kockara u Srbiji (posle reformi 2024) ili jasno dokumentovati da su podaci iz 2018 najnoviji dostupni.

#### Deliverables:
1. **Istraživački izveštaj** (5-7 strana):
   - Najnovija dostupna studija prevalence
   - Datum i metodologija studije
   - Glavni nalazi
   - Poređenje sa podacima iz 2018 (51k-93k)
   - Trendovi posle reformi 2024

2. **Preporuka** za novu studiju ako su podaci zastareli:
   - Opseg istraživanja
   - Metodologija
   - Budžet
   - Vremenski okvir

#### Potrebni resursi:
- Institut za javno zdravlje Srbije
- Medicinski fakulteti (studije zavisnosti)
- Beogradska klinika za lečenje zavisnosti
- Međunarodne baze podataka (WHO, EMCDDA)
- Akademske publikacije (PubMed, Google Scholar)

#### Istraživačka pitanja:
1. Postoji li studija POSLE 2018?
2. Da li su izmene zakona iz 2024 imale uticaj na prevalencu?
3. Kakvi su trendovi među mladima (ESPAD 2023/2024)?
4. Koliko je online kockanje uticalo na problematičko kockanje?

#### Output fajl:
`Prevalenca-Zavisnosti-Azurirani-Podaci.md`

---

## 🟠 PRIORITET 2: VEOMA VAŽNI SUBAGENTI

### SUBAGENT-06: Regulatorna Procena Uticaja (RIA) - Priprema

**Tip:** Ekonomski/Planski
**Prioritet:** 🟠 VEOMA VAŽAN
**Trajanje:** 5-7 dana
**Odgovoran:** AI Policy Analysis Agent

#### Zadatak:
Pripremiti detaljan **Terms of Reference (ToR)** dokument za spoljnu RIA studiju koju bi izvela nezavisna konsultantska kuća ili ekonomski institut.

#### Deliverables:
1. **ToR dokument** (15-20 strana) koji sadrži:
   - Pozadina i kontekst
   - Ciljevi RIA
   - Opseg istraživanja
   - Metodologija (predložena)
   - Deliverables od RIA
   - Kvalifikacije konsultanta
   - Budžet (procena)
   - Vremenski okvir

2. **Kratak izveštaj** (5 strana):
   - Lista potencijalnih institucija za RIA
   - Procena troškova
   - Preporuka za najbolji pristup

#### Opseg RIA (za ToR):
1. **Fiskalna analiza:**
   - Kvantifikacija prihoda (trenutno vs. aukcija)
   - Best/Base/Worst case scenariji
   - Break-even analiza

2. **Ekonomska analiza:**
   - Uticaj na konkurenciju (rizik oligopola)
   - Uticaj na zaposlenje
   - Uticaj na investicije

3. **Socijalna analiza:**
   - Uticaj na prevalencu problematičkog kockanja
   - Rizik online migracije
   - Geografska raspodela

4. **Administrativna analiza:**
   - Troškovi implementacije
   - Kapaciteti Uprave za igre na sreću
   - Kapaciteti 170+ opština

5. **Pravna analiza:**
   - Usklađenost sa Ustavom
   - Rizici od tužbi (domaćih i međunarodnih)

#### Potrebni resursi:
- RIA metodologija (OECD, EU standardi)
- Primeri RIA iz drugih sektora u Srbiji
- Lista konsultantskih kuća (ekonomski instituti, univerziteti)

#### Output fajl:
`ToR-Regulatorna-Procena-Uticaja.md`

---

### SUBAGENT-07: Komparativna Studija - Belgija, Italija, Holandija

**Tip:** Istraživački (uporedni)
**Prioritet:** 🟠 VEOMA VAŽAN
**Trajanje:** 7-10 dana
**Odgovoran:** AI Comparative Research Agent

#### Zadatak:
Izvršiti detaljnu komparativnu analizu sistema kvota/ograničenja u Belgiji, Italiji i Holandiji, sa fokusno na PRAKSU implementacije i EFEKTE.

#### Deliverables:
1. **Komparativni izveštaj** (25-35 strana) koji sadrži:
   - **Belgija sekcija:**
     - Kako funkcioniše sistem 600 fiksnih licenci?
     - Ko određuje kvotu (nacionalno/lokalno)?
     - Proces dodele licenci (aukcija/aplikacija?)
     - Koliko je trajala implementacija?
     - Problemi koji su nastali
     - Efekti na prevalencu kockanja
     - Fiskalni efekti

   - **Italija sekcija:**
     - Sistem 5,775 uplatno-isplatnih mesta
     - Koncesionarski model
     - Proces implementacije
     - Efekti

   - **Holandija sekcija:**
     - Državni monopol (Holland Casino)
     - Lokalna kontrola za automate
     - Opt-out mechanism
     - CRUKS registar (self-exclusion)
     - Efekti

2. **Izvođenje lekcija za Srbiju:**
   - Šta je funkcionisalo?
   - Šta nije funkcionisalo?
   - Koje modele Srbija može primeniti?
   - Koje greške izbegavati?

3. **Tabela uporednih indikatora:**
   - Broj objekata (pre/posle)
   - Prevalenca zavisnosti (pre/posle)
   - Fiskalni prihodi (pre/posle)
   - Vremenski okvir implementacije

#### Potrebni resursi:
- Belgian Gaming Commission (BGC) - izveštaji
- Agenzia delle Dogane e dei Monopoli (Italija)
- Kansspelautoriteit (Holandija)
- Akademske studije evaluacije
- Evropska komisija - gambling policy database
- WebFetch za pristup stranim dokumentima

#### Istraživačka pitanja:
1. Kako su određeni brojevi (600 u Belgiji, 5,775 u Italiji)?
2. Da li je bilo otpora od operatera? Kako je rešeno?
3. Koliko je trajala tranzicija sa starog na novi sistem?
4. Da li su korišćene prelazne odredbe? Kakve?
5. Kakvi su efekti na zavisnost bili MERENI?

#### Output fajl:
`Komparativna-Studija-Belgija-Italija-Holandija.md`

---

### SUBAGENT-08: Analiza Rizika Međunarodne Arbitraže

**Tip:** Pravni
**Prioritet:** 🟠 VEOMA VAŽAN
**Trajanje:** 5-7 dana
**Odgovoran:** AI International Law Research Agent

#### Zadatak:
Analizirati rizik od međunarodnih investicionih arbitraža (ICSID, etc.) ako Srbija jednostrano promeni pravila bez prelaznih odredbi i kompenzacije za stečena prava.

#### Deliverables:
1. **Pravni memo** (10-15 strana):
   - Relevantni međunarodni ugovori (BIT - Bilateral Investment Treaties)
   - Fair and Equitable Treatment (FET) standard
   - Precedenti (slični slučajevi u gaming industriji)
   - Potencijalni iznos odštete
   - Verovatnoća gubitka arbitraže

2. **Lista stranih investitora sa izloženošću:**
   - Flutter (MaxBet - 148M USD investicija 2023)
   - Drugi glavni igrači
   - Procena njihovog rizika za arbitražu

3. **Preporuke za mitigaciju rizika:**
   - Adekvatne prelazne odredbe
   - Kompenzacijski mehanizmi
   - Komunikacijska strategija

#### Potrebni resursi:
- ICSID case database
- BIT između Srbije i relevantnih zemalja (UK, Irska za Flutter)
- Investicije stranih operatera u Srbiji
- Precedenti iz drugih zemalja (npr. Španija - arbitraža zbog promene renewable energy zakona)

#### Istraživačka pitanja:
1. Koje zemlje imaju BIT sa Srbijom relevantne za gaming operatere?
2. Kakvi su bili ishodi sličnih arbitraža u drugim sektorima?
3. Koliko bi mogla biti odšteta u worst-case scenariju?
4. Kako su druge zemlje mitigirale ovaj rizik?

#### Output fajl:
`Analiza-Rizika-Medjunarodne-Arbitraze.md`

---

### SUBAGENT-09: Ustavnosudska Analiza - Detaljno

**Tip:** Pravni
**Prioritet:** 🟠 VEOMA VAŽAN
**Trajanje:** 7-10 dana
**Odgovoran:** AI Constitutional Law Agent

#### Zadatak:
Izvršiti **najdublju moguću** analizu ustavne održivosti predloga, sa detaljnom analizom svakog relevantnog člana Ustava i precedenata Ustavnog suda.

#### Deliverables:
1. **Ustavnopravna analiza** (30-40 strana):

   **Deo 1: Član po član analiza**
   - **Član 97** (nadležnosti Republike):
     - Tačan tekst
     - Tumačenje pojma "fiskalni sistem"
     - Tumačenje pojma "jedinstveno tržište"
     - Precedenti Ustavnog suda
     - Primenjivost na kockanje

   - **Član 177** (lokalna samouprava):
     - Šta spada u "poslove lokalnog značaja"?
     - Da li kockanje spada ili ne?
     - Precedenti

   - **Član 178** (prenos nadležnosti):
     - Uslovi za prenos sa Republike na opštine
     - Standard "efikasnijeg i racionalnijeg ostvarivanja prava"
     - Da li predlog ispunjava ovaj standard?

   - **Član 195** (hijerarhija propisa):
     - Sukob između ZoIS član 2 i predloženog ZoLS
     - Kako se rešava sukob zakona istog ranga?

   - **Član 203** (izmena Ustava):
     - Da li je potrebna ustavna izmena umesto zakonske?
     - Procedura i pragovi

   **Deo 2: Precedenti Ustavnog suda**
   - Lista svih relevantnih odluka
   - Analiza argumentacije
   - Primenjivost na ovaj slučaj

   **Deo 3: Finalna procena**
   - Verovatnoća da Ustavni sud proglasi neustavnim
   - Najranjiviji delovi predloga
   - Kako popraviti predlog da bude ustavan?

2. **Executive Summary** (2 strane) za donosioca odluke

#### Potrebni resursi:
- Ustav Republike Srbije (pun tekst)
- Baza odluka Ustavnog suda
- Stručna literatura o podeli nadležnosti
- Uporedni ustavno-pravni sistemi

#### Output fajl:
`Ustavnosudska-Analiza-Detaljna.md`

---

## 🟡 PRIORITET 3: VAŽNI SUBAGENTI (Dugoročno)

### SUBAGENT-10: Unapređenje Gemini Izveštaja

**Tip:** Dokumentacioni
**Prioritet:** 🟡 VAŽAN
**Trajanje:** 3-5 dana
**Odgovoran:** AI Document Editor Agent

#### Zadatak:
Ažurirati Gemini izveštaj primenom svih identifikovanih unapređenja iz Cross-Check dokumenta.

#### Deliverables:
1. **Novi verzija Gemini izveštaja** (cirilica) koja uključuje:

   **Dodati:**
   - ⭐ Nova sekcija: "Analiza člana 48 Zakona o referendumu"
   - Kvantitativna fiskalna analiza (kada bude dostupna iz SUBAGENT-03)
   - Ažurirani podaci o zavisnosti (iz SUBAGENT-05)
   - Disclaimer za zastarele podatke

   **Ukloniti/Kvalifikovati:**
   - Reddit thread iz bibliografije
   - Kvalifikovati medijske izvore ("za ilustraciju javnog mišljenja")

   **Unaprediti:**
   - Dodati konkretne matematičke projekcije umesto spekulacija

2. **Change log** dokument koji navodi sve promene

#### Potrebni input fajlovi:
- Originalni Gemini izveštaj
- Output iz SUBAGENT-01 (član 48)
- Output iz SUBAGENT-03 (fiskalna analiza)
- Output iz SUBAGENT-05 (zavisnost)

#### Output fajl:
`Analiza-predloga-zakona-Gemini-v2.md`

---

### SUBAGENT-11: Unapređenje Claude Izveštaja

**Typ:** Dokumentacioni
**Prioritet:** 🟡 VAŽAN
**Trajanje:** 3-5 dana
**Odgovoran:** AI Document Editor Agent

#### Zadatak:
Ažurirati Claude izveštaj primenom svih identifikovanih unapređenja.

#### Deliverables:
1. **Nova verzija Claude izveštaja** (latinica) koja uključuje:

   **Dodati:**
   - ⭐ Formalna bibliografija ("Works Cited" sekcija)
   - Kvantitativna fiskalna analiza (iz SUBAGENT-03)
   - Ažurirani podaci (iz SUBAGENT-05)

   **Zameniti:**
   - ❌ "<10%" bez metodologije
   - ✅ Scenario analiza (Scenario A: 0-5%, B: 10-20%, C: neizvesno)
   - Eksplicitno navesti: "Ovo je analitička procena, ne pravno mišljenje"

   **Ublažiti:**
   - "potpuno netačno" → "faktografski netačno"
   - Održati objektivnost

2. **Change log** dokument

#### Potrebni input fajlovi:
- Originalni Claude izveštaj
- Output iz SUBAGENT-03, 05

#### Output fajl:
`Claude-raw-v2.md`

---

### SUBAGENT-12: Unapređenje Meta-Analize

**Tip:** Dokumentacioni
**Prioritet:** 🟡 VAŽAN
**Trajanje:** 3-5 dana
**Odgovoran:** AI Document Editor Agent

#### Zadatak:
Ažurirati Meta-Analizu sa svim novim nalazima.

#### Deliverables:
1. **Nova verzija Meta-Analize** koja uključuje:

   **Dodati:**
   - ⭐⭐⭐ Nova sekcija: "Kvantitativna fiskalna analiza" (iz SUBAGENT-03)
   - Update Addendum-a sa nalazima iz SUBAGENT-01, 02
   - Ažurirani podaci
   - Ocena pouzdanosti svih izvora (Gemini)

   **Skratiti:**
   - Razmotriti Executive Summary + Appendices format
   - Trenutno 20,000 reči je možda previše

2. **Change log**

#### Output fajl:
`Meta-Analiza-Izvestaja-v2.md`

---

### SUBAGENT-13: Kreiranje Executive Summary za Donosioca Odluke

**Typ:** Dokumentacioni
**Prioritet:** 🟡 VAŽAN
**Trajanje:** 2-3 dana
**Odgovoran:** AI Policy Brief Writer Agent

#### Zadatak:
Kreirati **ultra-koncizni** dokument (2-4 strane) za donosioca odluke koji sumira SVE analize i daje jasne preporuke.

#### Deliverables:
1. **Policy Brief** (2-4 strane) sa sekcijama:

   **Strana 1: Situacija u jednoj minuti**
   - Problem koji Inicijativa identifikuje (3 rečenice)
   - Predloženo rešenje (2 rečenice)
   - Glavni problemi sa predlogom (bullet points)
   - Preporuka (1 rečenica)

   **Strana 2: Pravni rizici**
   - Član 48 (proceduarna barijera)
   - Ustavne barijere (član 97, 177)
   - Verovatnoća uspeha: 5-15%

   **Strana 3: Ekonomski efekti**
   - Fiskalna projekcija (best/base/worst)
   - Rizici (konsoldacija, arbitraža)

   **Strana 4: Akcije**
   - Hitno: Pravno mišljenje o članu 48 (2 nedelje)
   - Ako prođe: RIA (2 meseca)
   - Alternativa: Razmotriti nacionalnu aukciju

2. **Vizualna infografika** (1 strana):
   - Dijagram odlučivanja
   - Ključne statistike
   - Timeline

#### Ton:
- Objektivan, ne advokatski
- Bez stručnog žargona
- Akciono orijentisan

#### Output fajlovi:
1. `Executive-Summary-Donosilac-Odluke.md`
2. `Infografika-Pregled.png` (ako moguće)

---

### SUBAGENT-14: Kreiranje Prezentacije za Narodnu Skupštinu

**Tip:** Dokumentacioni
**Prioritet:** 🟡 VAŽAN
**Trajanje:** 3-4 dana
**Odgovoran:** AI Presentation Designer Agent

#### Zadatak:
Kreirati PowerPoint ili Google Slides prezentaciju (~20-25 slajdova) koja sumira sve nalaze za prezentaciju u Narodnoj skupštini.

#### Deliverables:
1. **PowerPoint prezentacija** sa sekcijama:

   **Slajd 1-3: Uvod**
   - Problem koji Inicijativa identifikuje
   - Statistika (Srbija drugo mesto, 2,921 kladionica)
   - Legitimnost problema

   **Slajd 4-8: Predloženo rešenje**
   - Šta Inicijativa predlaže?
   - Mehanizam (lokalne kvote + aukcije)
   - Ciljevi (demokracija, fiskalni prihod, harm reduction)

   **Slajd 9-15: Identifikovani problemi**
   - Član 48 (procedurana barijera)
   - Ustavne barijere
   - Strukturni problemi
   - Fiskalni rizici
   - Socijalni rizici (online migracija)

   **Slajd 16-18: Uporedni primeri**
   - Albanija (neuspeh zabrane)
   - Belgija, Italija, Holandija (uspešni modeli)

   **Slajd 19-22: Alternative**
   - Nacionalna aukcija
   - Pojačano enforcement
   - Opt-out mechanism

   **Slajd 23-25: Preporuke i sledeći koraci**
   - Hitna pravna provera
   - RIA
   - Alternativni model

2. **Speaker notes** za svaki slajd

#### Vizualni stil:
- Profesionalan, ne flashy
- Maksimalno teksta: 5-7 bullet points po slajdu
- Grafikoni i tabele gde moguće
- Konzistentna šema boja

#### Output fajl:
`Prezentacija-Narodna-Skupstina.pptx` (ili .md sa strukturom)

---

### SUBAGENT-15: Monitoring Plan za Novi Zeland 2026 Aukciju

**Tip:** Istraživački (dugoročan)
**Prioritet:** 🟡 VAŽAN
**Trajanje:** Ongoing (check-in svaka 3 meseca)
**Odgovoran:** AI Monitoring Agent

#### Zadatak:
Pratiti planiranu prvu veliku gambling license aukciju u Novom Zelandu (2026) kao test case i izvući lekcije za Srbiju.

#### Deliverables:
1. **Quarterly Update Reports** (svaka 3 meseca):
   - Status implementacije u Novom Zelandu
   - Rezultati aukcije (kada se dese)
   - Cene postihnute
   - Broj učesnika
   - Problemi koji nastanu

2. **Finalni izveštaj** (nakon završetka aukcije):
   - Kompletna analiza NZ modela
   - Lekcije za Srbiju
   - Preporuke za adaptaciju

#### Istraživačka pitanja:
1. Kakav je trostepeni proces (EOI → Auction → License)?
2. Koliko je 15 dozvola dovoljno za celu zemlju?
3. Kakve su bile postignute cene?
4. Da li je bilo problema ili žalbi?
5. Kakav je bio uticaj na prevalencu kockanja?

#### Potrebni resursi:
- NZ Department of Internal Affairs
- NZ gambling regulators
- Akademske evaluacije (kada budu objavljene)

#### Timeline:
- Q1 2025: Pre-auction analiza
- Q2-Q3 2025: Monitoring EOI i auction procesa
- Q4 2025/Q1 2026: Post-auction analiza
- Q2-Q4 2026: Evaluacija efekata

#### Output fajlovi:
1. `NZ-Aukcija-Update-Q1-2025.md`
2. `NZ-Aukcija-Update-Q2-2025.md`
3. ... (quarterly)
4. `NZ-Aukcija-Finalni-Izvestaj.md`

---

## KOORDINACIJA I DEPENDENCIES

### Dependency Map:

```
PRIORITET 1 (Paralelno):
├─ SUBAGENT-01 (Član 48) ────┐
├─ SUBAGENT-02 (Precedenti) ──┤
├─ SUBAGENT-04 (Trenutni prihodi) ─┐
└─ SUBAGENT-05 (Zavisnost) ────────┘
                                    │
                                    ▼
                    SUBAGENT-03 (Fiskalni model)
                                    │
                                    │ (Čeka SUBAGENT-04)
                                    ▼
                            [Odluka o članu 48]
                                    │
                        ┌───────────┴───────────┐
                    Ako PROĐE              Ako NE PROĐE
                        │                       │
                        ▼                       ▼
                 PRIORITET 2              KRAJ (ili alternative)
                        │
        ┌───────────────┼───────────────┐
        │               │               │
   SUBAGENT-06      SUBAGENT-07    SUBAGENT-08
     (RIA)        (Komparativna)  (Arbitraža)
                        │
                        │
                        ▼
                   SUBAGENT-09
                  (Ustavni sud)
                        │
                        ▼
                  PRIORITET 3
                        │
        ┌───────────────┼───────────────┬───────────────┐
        │               │               │               │
   SUBAGENT-10     SUBAGENT-11    SUBAGENT-12    SUBAGENT-13
   (Gemini v2)     (Claude v2)   (Meta v2)    (Executive)
                        │
                        └──────────────┬────────────────┘
                                       ▼
                                 SUBAGENT-14
                                (Prezentacija)
```

### Paralelizacija:

**Faza 1 (Nedelje 1-2): Paralelno izvršiti**
- SUBAGENT-01, 02, 04, 05 (svi nezavisni)

**Faza 2 (Nedelje 2-3): Nakon Faze 1**
- SUBAGENT-03 (čeka podatke iz 04)

**Faza 3 (Odluka): Nakon Faze 2**
- Pravni revizor odlučuje o članu 48

**Faza 4 (Nedelje 4-10): Ako prođe član 48, paralelno**
- SUBAGENT-06, 07, 08, 09

**Faza 5 (Nedelje 10-12): Dokumentacija, paralelno**
- SUBAGENT-10, 11, 12

**Faza 6 (Nedelje 12-14): Finalizacija**
- SUBAGENT-13, 14

**Ongoing:**
- SUBAGENT-15 (NZ monitoring)

---

## RESOURCE REQUIREMENTS

### Za AI Izvršenje:

**Tools potrebni:**
- ✅ WebFetch (za pravna dokumenta, studije)
- ✅ Read/Write (za kreiranje dokumenta)
- ✅ Grep/Glob (za pretragu postojećih fajlova)
- ⚠️ Excel/Spreadsheet tool (za SUBAGENT-03 model) - možda Google Sheets via API?

**Eksterni resursi:**
1. **Pravni:**
   - Paragraf.rs (pristup)
   - Arhiva Narodne skupštine (možda FOI zahtev)
   - Ustavni sud baza odluka

2. **Ekonomski:**
   - Uprava za igre na sreću (godišnji izveštaji)
   - Ministarstvo finansija (budžet)

3. **Međunarodni:**
   - Belgian Gaming Commission
   - Agenzia delle Dogane e dei Monopoli (Italija)
   - Kansspelautoriteit (Holandija)
   - NZ Department of Internal Affairs

4. **Akademski:**
   - Google Scholar
   - PubMed
   - SSRN
   - Institucionalni repozitorijumi

---

## TIMELINE SUMMARY

| Prioritet | Subagenti | Trajanje | Outcome |
|-----------|-----------|----------|---------|
| 🔴 P1 | 01-05 | 1-5 dana | Odluka o članu 48 + osnovni podaci |
| 🟠 P2 | 06-09 | 5-10 dana | Duboka analiza (samo ako P1 prođe) |
| 🟡 P3 | 10-14 | 3-7 dana | Finalni dokumenti |
| 🟢 Ongoing | 15 | 12-18 meseci | NZ monitoring |

**Ukupno za kompletnu analizu (P1+P2+P3):** ~4-6 nedelja

**Fast-track (samo P1 + Executive Summary):** ~2 nedelje

---

## EXECUTION STRATEGY

### Opcija A: Sekvencijalno (sigurnije, sporije)
Izvršiti subagente jedan po jedan prema prioritetu.
- **Vreme:** 6-8 nedelja
- **Rizik:** Nizak
- **Best for:** Konzervativni pristup

### Opcija B: Paralelno (brže, kompleksnije)
Izvršiti sve P1 subagente istovremeno.
- **Vreme:** 2-3 nedelje za P1
- **Rizik:** Umeren (koordinacija)
- **Best for:** Hitne situacije

### Opcija C: Hybrid (preporučeno)
- P1 subagenti paralelno (sem 03 koji čeka 04)
- Odluka o članu 48
- P2 subagenti paralelno ako potrebno
- P3 sekvencijalno za finalizaciju
- **Vreme:** 3-5 nedelja
- **Rizik:** Nizak
- **Best for:** Balans brzina/kvalitet

---

## KVALITETNA KONTROLA

**Za svaki subagent:**
1. ✅ Peer review od drugog AI agenta
2. ✅ Fact-check svih ključnih tvrdnji
3. ✅ Citiranje svih izvora
4. ✅ Executive summary na početku svakog dokumenta
5. ✅ Clear methodology section

**Kriterijumi uspeha:**
- Svi deliverables isporučeni na vreme
- Svi izvori verifikovani i citirani
- Nijedna spekulacija bez disclaimera
- Sve kvantitativne projekcije sa transparentnom metodologijom
- Finalni dokumenti dostupni za javnost

---

**Pripremio:** AI Task Planning Agent
**Datum:** 18. novembar 2025
**Baziran na:** Cross-Check-Sinteza-Final.md
**Status:** SPREMAN ZA IZVRŠENJE

---

## SLEDEĆI KORAK

**Za pokretanje izvršenja:**
```
Odabrati prioritet:
- "Izvršiti sve P1 subagente" (hitno, 2 nedelje)
- "Izvršiti sve subagente" (kompletno, 6 nedelja)
- "Izvršiti samo [broj] subagent" (individualno)
```

**Preporuka:** Početi sa P1 (SUBAGENT-01 do 05) i nakon završetka odlučiti o P2/P3 na osnovu rezultata.
