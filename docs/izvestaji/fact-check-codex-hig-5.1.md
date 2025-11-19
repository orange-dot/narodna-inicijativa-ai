# Fact Check - Codex High 5.1

**Datum:** 19. novembar 2025  
**Analiticar:** Codex (Fact-check pod-agent)  
**Obuhvaceni fajlovi:** `README.md`, `docs/izvestaji/Meta-Analiza-V2.md`, `docs/pravna-analiza/*.md`, `docs/fiskalna-analiza/*.md`, `docs/istrazivanja/Prevalenca-Zavisnosti-Azurirani-Podaci.md`, `docs/pravna-analiza/ICSID-Arbitraza-Rizici.md`

## Domet i metodologija
- Mapirane su tvrdnje iz README-ja, Meta-Analize V2 i tematskih memo dokumenata (pravo, fiskalno, ICSID).
- Za svaku tvrdnju pronadjen je javni izvor ili je oznaceno da se oslanja iskljucivo na interne pretpostavke.
- Korisceni su proverljivi javni podaci (Nova Ekonomija, World Bank API, medijski clanci) i zvanicni propisi (Paragraf).
- Status legenda: OK = potvrdeno; PART = delimicno tacno ili zastarelo; TBD = nema dokaza; NOK = netacno/kontradiktorno.

## Rezime nalaza
- [OK] Podatak o 2.921 kladionici i drugo mesto u Evropi potvrdjuje Nova Ekonomija; izracun gustine (44,3/100k) je konzistentan sa World Bank populacijom.
- [PART] Ukupni prihodi od 320 mil. EUR su potvrdeni, ali udeo u BDP vise nije 0,53% (sa BDP-om 2024. od ~89 mlrd USD udeo je 0,36-0,39%).
- [PART] Procena 51-93 hiljade problematicnih kockara zasnovana je na Batut studiji iz 2018. i nije osvezena.
- [TBD] Projekcija fiskalnog gubitka od 45% i verovatnoca uspeha 3-15% nemaju dokumentovanu metodologiju ni ulazne parametre.
- [OK] Pravni rizici (clan 48 Zakona o referendumu, clan 97 Ustava, clan 7/8 Zakona o igrama na srecu) potvrdjeni su u zvanicnim tekstovima.
- [PART] ICSID analiza tacno prepoznaje prisustvo stranog investitora (Flutter/MaxBet), ali procene odstete (200-500 mil. EUR) nisu potkrepljene.

## Tabela kriticnih tvrdnji

| # | Tvrdnja | Izvor u projektu | Status | Nalaz / dokaz |
|---|--------|------------------|--------|---------------|
| 1 | Srbija ima ~2.921 kladionicu (44,3/100k); drugo mesto u Evropi | `README.md`, `Meta-Analiza-V2.md` | OK | Nova Ekonomija (12.05.2025) navodi 2.921 objekat i drugo mesto u Evropi; World Bank populacija 2024 (6,59M) daje 44,3/100k.[^1][^2] |
| 2 | Ukupni prihodi 320 mil. EUR = 0,53% BDP | `README.md`, `docs/fiskalna-analiza/Trenutni-Fiskalni-Prihodi-SIMPLE.md` | PART | Nova Ekonomija potvrduje 177 mil. EUR iz naknada i ~320 mil. EUR ukupno, ali World Bank BDP 2023/2024 spusta udeo na 0,36-0,39%.[^1][^3] |
| 3 | 51-93k problematicnih kockara (0,8-1,4% populacije) | `README.md`, `docs/istrazivanja/Prevalenca-Zavisnosti-Azurirani-Podaci.md` | PART | Nova Ekonomija (21.05.2025) citira Batut 2018 kao poslednji podatak; nema posle-2018 baseline-a.[^4] |
| 4 | Fiskalni model -> gubitak -143 mil. EUR (-45%) | `Meta-Analiza-V2.md`, `FISKALNI-MODEL-README.md` | TBD | Ulazne vrednosti (elasticnost GGR, aukcijske cene) nisu dokumentovane, niti postoje FOI podaci koji bi kalibrisali model. |
| 5 | Verovatnoca uspeha inicijative 5-15% / 3-5% | `README.md`, `Meta-Analiza-V2.md` | TBD | Procene nisu potkrepljene metodom (nema scoring tabele, presedana ili odluka Ustavnog suda). |
| 6 | Clan 48 Zakona o referendumu zabranjuje fiskalne zakone | `docs/pravna-analiza/Pravni-Memo-Clan48-Verifikacija.md` | OK | Zvanicni tekst Zakona (Sl. glasnik 111/2021) eksplicitno navodi "poreski i drugi finansijski zakoni" kao zabranjenu temu.[^5] |
| 7 | Clan 97 Ustava + Zakon o igrama na srecu -> licenciranje je republicko | `Pravni-Memo-Clan48-Verifikacija.md`, `docs/pravna-analiza/Precedenti-Clan48-Analiza.md` | OK | Ustav RS (cl. 97 tacka 6) navodi poreski sistem kao republicki; Zakon o igrama cl. 7-8 propisuje da je priredivanje iskljucivo pravo Republike.[^6][^7] |
| 8 | Flutter/MaxBet 51% za 141 mil. EUR (ICSID rizik) | `docs/pravna-analiza/ICSID-Arbitraza-Rizici.md` | PART | GamblingNews (27.09.2023) potvrduje akviziciju, ali procena odstete 200-500 mil. EUR nije poduprta primerima ili BIT izvorom.[^8] |
| 9 | EGBA 2023 je izvor svih fiskalnih vrednosti | `README.md`, `FISKALNI-MODEL-METADATA.md` | TBD | Direktan pristup EGBA izvestaju nije moguc (download vraca HTML). Bez tacnog citata, tvrdnja ostaje neproverljiva. |
| 10 | EU prosek 9 kladionica/100k | `README.md` | TBD | Nije pronadjen javni dataset koji potvrdjuje EU prosek; navod nema referencu. |

## Detaljna zapazanja

### 1. Trzisna struktura i gustina
- Nova Ekonomija navodi 2.921 kladionicu i uporedne odnose prema Italiji, UK i Spaniji. Sa World Bank populacijom za 2024. izracun 44,3 kladionice/100k stanovnika se uklapa u README tvrdnju.
- EU prosek 9/100k nije potvrdjen. Preporuka: objaviti izvor ili ukloniti navod.

### 2. Fiskalni parametri
- Nova Ekonomija jasno izdvaja 177 mil. EUR (naknade) i ~320 mil. EUR ukupno (ukljucujuci poreze). 
- Tvrdnja da taj prihod iznosi 0,53% BDP je zastarela; BDP 2023-2024 (81-89 mlrd USD) daje 0,36-0,39%. Potrebno je azurirati relativne pokazatelje i navesti godinu na koju se odnose.
- Model koji predvidja -143 mil. EUR bez detalja o elastičnosti GGR ili ocekivanim aukcijskim cenama predstavlja scenario, ne cinjenicu.

### 3. Javno zdravlje i prevalenca
- README i rezimei i dalje koriste 51-93k kao fakt, iako `docs/istrazivanja/Prevalenca-Zavisnosti-Azurirani-Podaci.md` navodi da podaci ne postoje posle 2018.
- Clanak "Nevidljiva mreza zavisnosti" potvrdjuje da strucnjaci rade sa pretpostavkama (~50k). Potrebno je eksplicitno oznaciti da je indikator zastareo i planirati novo istrazivanje.

### 4. Pravni okvir
- Clan 48 Zakona o referendumu i clan 108 Ustava ponavljaju zabranu "poreskih i drugih finansijskih zakona" za referendum, sto potvrdjuje zakljucke pravnog memo-a.
- Clan 97 Ustava i clan 7 Zakona o igrama naglasavaju iskljucivo pravo Republike na priredivanje i nadzor, pa prost prenos licenciranja na lokalni nivo vodi u koliziju zakona istog ranga.

### 5. ICSID i investicioni rizik
- Flutter (UK/Irska) je kupio 51% MaxBeta za 141 mil. EUR, pa postoje strani investitori koji bi mogli koristiti BIT mehanizme.
- Međutim, procene odstete (200-500 mil. EUR) ne navode metodologiju niti uporedne presude. ICSID memo treba dopuniti konkretnim BIT referencama i DCF/benchmark kalkulacijama.

### 6. Kvantitativne procene verovatnoce
- README navodi "5-15%", a Meta-Analiza V2 "3-5%" verovatnoce uspeha bez ikakvog obrazlozenja.
- Preporuka: ukloniti procentualne tvrdnje ili ih oznaciti kao subjektivne dok se ne obezbedi metod (npr. scoring matrica, poređenje sa ranijim inicijativama).

### 7. EGBA kao izvor
- Vise fajlova citira "EGBA Report 2023", ali linkovi vode na HTML 404 zbog ogranicenja pristupa. Dok se ne pribavi lokalna kopija ili precizan citat, brojke treba da se pozivaju na dostupne domace izvore (npr. Nova Ekonomija, Ministarstvo finansija).

## Preporuceni sledeci koraci
1. **Azurirati finansijske razmere** – navesti najnovije BDP i kurs, i jasno obeleziti godinu podataka.
2. **Formalizovati pravne fusnote** – svaki put kada se citira clan 48/97 ili Zakon o igrama dodati referencu na zvanicni tekst.
3. **Pokrenuti novo istrazivanje prevalencije** – bez empirijskih podataka posle 2018. nemoguce je proceniti efekat intervencija.
4. **Dokumentovati metodologije** – fiskalni modeli i procene verovatnoce moraju sadrzati ulazne parametre i izvore; u suprotnom ih tretirati kao scenario.
5. **Prosiriti ICSID analizu** – navesti relevantne BIT ugovore i nacine izracuna potencijalne odstete pre navodjenja raspona 200-500 mil. EUR.

## Evidencija izvora
[^1]: Nova Ekonomija, "Drzava zaradjuje stotine miliona evra od kladionica i kockarnica", 12. maj 2025.  
[^2]: World Bank API, indikator `SP.POP.TOTL`, Srbija 2024 (6.587.202).  
[^3]: World Bank API, indikator `NY.GDP.MKTP.CD`, Srbija 2023-2024 (81,34-89,08 mlrd USD).  
[^4]: Nova Ekonomija, "Nevidljiva mreza zavisnosti: Kocka kao drzavno stimulisan porok", 21. maj 2025.  
[^5]: Zakon o referendumu i narodnoj inicijativi ("Sl. glasnik RS" 111/2021), clan 48 (Paragraf.rs).  
[^6]: Ustav Republike Srbije ("Sl. glasnik RS" 98/2006), clan 97 tacka 6 i clan 108 (Paragraf.rs).  
[^7]: Zakon o igrama na srecu ("Sl. glasnik RS" 18/2020, 94/2024), clan 7 i 8 (Paragraf.rs).  
[^8]: GamblingNews, "Flutter Agrees to Acquire 51% Stake in MaxBet via $149M Deal", 27. septembar 2023.

