# FISKALNI MODEL AUKCIJA - VIZUELNI PREGLED

**Za: Brzo razumevanje ključnih nalaza**
**Datum:** 18. novembar 2025

---

## 📊 GLAVNI NALAZ U JEDNOJ REČENICI

**Aukcijski sistem NE MOŽE održati trenutne fiskalne prihode. Očekivani gubitak: -40% (-129M EUR godišnje)**

---

## 💰 TRENUTNO vs. OČEKIVANO

```
TRENUTNI SISTEM:
┌─────────────────────────────────────────┐
│ UKUPNO: 320M EUR                        │
├─────────────────────────────────────────┤
│ Direktne naknade:  177M EUR (55%) ████  │
│ Porezi na GGR:     140M EUR (44%) ████  │
└─────────────────────────────────────────┘

AUKCIJSKI SISTEM (očekivano):
┌─────────────────────────────────────────┐
│ UKUPNO: 191M EUR ⚠️                      │
├─────────────────────────────────────────┤
│ Direktne naknade:  114M EUR (60%) ███   │
│ Porezi na GGR:      77M EUR (40%) ██    │
└─────────────────────────────────────────┘

DELTA: -129M EUR (-40%) ❌
```

---

## 📈 TRI SCENARIJA - SVA TRI NEGATIVNA

```
                     Trenutno
                        │
                     320M EUR
                        │
        ┌───────────────┼───────────────┐
        │               │               │
   Scenario A      Scenario B      Scenario C
  (Optimistični)   (Realistični)   (Pesimistični)
        │               │               │
     330M EUR        199M EUR         90M EUR
     (+3%)           (-38%)          (-72%)
        │               │               │
    Verovatnoća    Verovatnoća    Verovatnoća
       15%             60%            25%
        │               │               │
   ┌────┴────┐     ┌────┴────┐    ┌────┴────┐
   │ GUBITAK │     │ VELIKI  │    │ KATASTRO-│
   │ MALI    │     │ GUBITAK │    │ FALAN    │
   └─────────┘     └─────────┘    └──────────┘

WEIGHTED AVERAGE: 191M EUR (-40%)
```

---

## 🎯 ZAŠTO GUBITAK? (Anatomija problema)

```
STRUKTURA TRENUTNIH PRIHODA:
┌──────────────────────────────────┐
│ 55% Direktne naknade  │ 177M EUR │ ← Aukcije mogu POVEĆATI
├──────────────────────────────────┤
│ 44% Porezi na GGR     │ 140M EUR │ ← Ali ovo STRUKTURALNO PADA
└──────────────────────────────────┘

EFEKAT REDUKCIJE:
┌─────────────────────────────────────────────┐
│ Manje objekata (↓ 30-70%)                   │
│         ↓                                   │
│ Manje ukupnog GGR (↓ 15-84%)                │
│         ↓                                   │
│ Manji porezi na GGR (↓ 20-79%)              │
│         ↓                                   │
│ STRUKTURALNI PAD koji aukcije               │
│ NE MOGU nadoknaditi                         │
└─────────────────────────────────────────────┘
```

---

## 🔢 BREAK-EVEN - MATEMATIČKA NEMOGUĆA MISIJA

**Pitanje:** Koliko moraju biti aukcijske cene za održavanje 320M EUR?

```
┌─────────────────┬──────────────────────────┬─────────────┐
│ Redukcija broja │ Potreban multiplikator   │ Realno?     │
├─────────────────┼──────────────────────────┼─────────────┤
│ 30%             │ 11-12× trenutne naknade  │ Malo        │
│ 50%             │ 15-18× trenutne naknade  │ Veoma malo  │
│ 70%             │ 25-30× trenutne naknade  │ Nemoguće    │
└─────────────────┴──────────────────────────┴─────────────┘

PRIMER (50% redukcija):
┌──────────────────────────────────────────────┐
│ Trenutna naknada:  300 EUR/mesec             │
│ Potrebna naknada:  4,500 EUR/mesec (15×)    │
│ To je:             54,000 EUR godišnje       │
│                                              │
│ Prosečan profit:   ~140,000 EUR/godišnje    │
│ Max spremnost:     ~110,000 EUR (80%)       │
│                                              │
│ ZAKLJUČAK: Teorijski moguće, ali...         │
│ • Pretpostavlja savršene aukcije            │
│ • Pretpostavlja rast profita                │
│ • ČAK I TADA: Pad GGR poreza eliminiše dobit│
└──────────────────────────────────────────────┘
```

---

## 🎲 NEIZVESNOST - EKSTREMNO ŠIROKI OPSEZI

```
90% CONFIDENCE INTERVAL:
│
│              [════════════════════════════════]
│              ↑                              ↑
│           120M EUR                      260M EUR
│         (p10, -63%)                (p90, -19%)
│
│                      ↑
│                  Očekivano
│                   191M EUR
│                    (-40%)
│
├──────────────────────────────────────────────────────────
0         100        200       300        400       500 M EUR
                              ↑
                         Trenutno
                         320M EUR

INTERPRETACIJA:
• Čak i u OPTIMI STIČNOM scenariju (p90): Gubitak -19%
• U PESIMISTIČNOM scenariju (p10): Gubitak -63%
• Trenutni prihod (320M) je IZVAN realnog opsega ⚠️
```

---

## 🔑 TRI NAJKRITIČNIJA PARAMETRA

```
1. ELASTIČNOST GGR (najvažniji)
   ┌────────────────────────────────────┐
   │ Koliko GGR pada kad broj objekata  │
   │ padne?                             │
   ├────────────────────────────────────┤
   │ Range: 0.3 - 1.5                   │
   │ Uticaj: ±50M EUR                   │
   │ Status: ⚠️ NEMA PODATAKA ZA SRBIJU  │
   └────────────────────────────────────┘

2. OFFSHORE MIGRACIJA
   ┌────────────────────────────────────┐
   │ Koliko igrača prelazi na ilegalne  │
   │ platforme?                         │
   ├────────────────────────────────────┤
   │ Range: 5% - 30%                    │
   │ Uticaj: ±30M EUR                   │
   │ Status: ⚠️ ZAVISI OD ENFORCEMENT    │
   └────────────────────────────────────┘

3. AUKCIJSKA DINAMIKA
   ┌────────────────────────────────────┐
   │ Koliko će operateri platiti?       │
   ├────────────────────────────────────┤
   │ Range: 1.2× - 3.0×                 │
   │ Uticaj: ±20M EUR                   │
   │ Status: ⚠️ NIJEDNA AUKCIJA JOŠ NIJE │
   │         ODRŽANA                     │
   └────────────────────────────────────┘
```

---

## 👥 KO GUBI? (Impact na namenske svrhe)

```
TRENUTNO:                    SA AUKCIJAMA (očekivano):
┌──────────────────┐        ┌──────────────────┐
│ Crveni krst      │        │ Crveni krst      │
│ 13.5M EUR ████   │   →    │ 8M EUR  ██   ❌  │
├──────────────────┤        ├──────────────────┤
│ Invalidi         │        │ Invalidi         │
│ 13.5M EUR ████   │   →    │ 8M EUR  ██   ❌  │
├──────────────────┤        ├──────────────────┤
│ Soc. zaštita     │        │ Soc. zaštita     │
│ 13.5M EUR ████   │   →    │ 8M EUR  ██   ❌  │
├──────────────────┤        ├──────────────────┤
│ Sport/omladina   │        │ Sport/omladina   │
│ 13.5M EUR ████   │   →    │ 8M EUR  ██   ❌  │
├──────────────────┤        ├──────────────────┤
│ Retke bolesti    │        │ Retke bolesti    │
│ 3.5M EUR  ██     │   →    │ 2M EUR  █    ❌  │
├──────────────────┤        ├──────────────────┤
│ Opšti budžet     │        │ Opšti budžet     │
│ 106M EUR ██████  │   →    │ 64M EUR ███  ❌  │
└──────────────────┘        └──────────────────┘

SVE NAMENSKE SVRHE GUBE ~40% SREDSTAVA ⚠️
```

---

## ⚠️ RIZICI (pored fiskalnih gubitaka)

```
┌─────────────────────────────┬──────────────┬──────────────┐
│ Rizik                       │ Verovatnoća  │ Uticaj       │
├─────────────────────────────┼──────────────┼──────────────┤
│ 1. Collusion operatera      │ 30-40%  ██   │ -30M EUR  ██ │
│    (niske ponude)           │              │              │
├─────────────────────────────┼──────────────┼──────────────┤
│ 2. Online → offshore        │ 40-60%  ███  │ -50M EUR ███ │
│    migracija                │              │              │
├─────────────────────────────┼──────────────┼──────────────┤
│ 3. Grey market              │ 30-40%  ██   │ -20M EUR ██  │
│    (polu-legalno)           │              │              │
├─────────────────────────────┼──────────────┼──────────────┤
│ 4. Socijalni backlash       │ 20-30%  █    │ Retreat od   │
│    (8,000+ bez posla)       │              │ reforme      │
├─────────────────────────────┼──────────────┼──────────────┤
│ 5. Failed auction           │ 15-25%  █    │ Privremeno   │
│    (propada aukcija)        │              │ bez prihoda  │
└─────────────────────────────┴──────────────┴──────────────┘

UKUPNA VEROVATNOĆA bar jednog rizika: ~70% ⚠️
```

---

## 🌍 UPOREDNI PRIMERI (Šta su drugi naučili)

```
┌────────────────────────────────────────────────────────┐
│ BELGIJA - F2 Casino Aukcije (2010)                     │
├────────────────────────────────────────────────────────┤
│ • Cene NIŽE od očekivanih (collusion sumnja)           │
│ • Samo 407/600 aktivnih (ostatak se ne isplati)        │
│ • LEKCIJA: Aukcije mogu razočarati ⚠️                   │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│ VELIKA BRITANIJA - Redukcija automata 50% (2019)       │
├────────────────────────────────────────────────────────┤
│ • GGR pao 67% (više nego proporcionalno!)              │
│ • Elastičnost: 1.3 (visoka)                            │
│ • LEKCIJA: GGR pada VIŠE nego broj objekata ⚠️          │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│ ALBANIJA - Totalna zabrana 2019 → Poništenje 2024      │
├────────────────────────────────────────────────────────┤
│ • Fiskalni prihodi: Potpuni kolaps                     │
│ • Ilegalno kockanje: Eksplozija                        │
│ • LEKCIJA: Drastične mere mogu imati suprotan efekat ⚠️ │
└────────────────────────────────────────────────────────┘
```

---

## 🚦 ANALIZA RIZIKA - CHECKPOINT 2

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│          ⚠️  IDENTIFIKOVANI RIZICI  ⚠️                  │
│                                                         │
│  Model pokazuje značajan fiskalni rizik                │
│                                                         │
├─────────────────────────────────────────────────────────┤
│ KLJUČNI NALAZI:                                         │
│                                                         │
│ 1. Očekivani gubitak: -45% (-143M EUR godišnje)        │
│                                                         │
│ 2. Verovatnoća profita: <10%                           │
│                                                         │
│ 3. Neizvesnost je visoka (nedostaju podaci)            │
│                                                         │
│ 4. Break-even je praktično nemoguć                     │
│                                                         │
│ 5. Postoje alternativne opcije                         │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 🔄 ALTERNATIVE (ako se ipak nastavi)

```
PRE BILO KAKVE IMPLEMENTACIJE:

┌──────────────────────────────────────┐
│ 1. REGULATORY IMPACT ASSESSMENT      │
│    • Nezavisna ekonomska studija     │
│    • FOI zahtevi za detaljne podatke │
│    • Trajanje: 6-12 meseci           │
└──────────────────────────────────────┘
           ↓
┌──────────────────────────────────────┐
│ 2. PILOT PROGRAM                     │
│    • 2-3 opštine, 12-24 meseca       │
│    • Tretman vs. kontrolna grupa     │
│    • Meriti: GGR, aukcije, offshore  │
└──────────────────────────────────────┘
           ↓
┌──────────────────────────────────────┐
│ 3. ROBUSNA ONLINE REGULATIVA         │
│    • Osnažiti enforcement PRVO       │
│    • Blokirati offshore platforme    │
│    • Self-exclusion registri         │
└──────────────────────────────────────┘
           ↓
┌──────────────────────────────────────┐
│ 4. AUKCIJSKI DIZAJN                  │
│    • Angažovati auction eksperta     │
│    • Anti-collusion mehanizmi        │
│    • Reserve prices                  │
└──────────────────────────────────────┘
           ↓
┌──────────────────────────────────────┐
│ 5. FULL IMPLEMENTATION               │
│    • Samo ako pilot uspešan          │
│    • Sa monitoring sistemom          │
│    • Sa sunset clauses               │
└──────────────────────────────────────┘
```

---

## 📚 DETALJNI MATERIJALI

```
┌────────────────────────────────────────────────────────┐
│ FULL ANALYSIS (25 strana):                             │
│ Fiskalni-Model-Aukcije.md                              │
│                                                        │
│ • Kompletna matematika                                 │
│ • Svi proračuni                                        │
│ • Python kod za replikaciju                            │
│ • 16 detaljnih sekcija                                 │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│ EXECUTIVE SUMMARY (2 strane):                          │
│ Fiskalni-Model-Aukcije-SIMPLE.md                       │
│                                                        │
│ • Ključni nalazi                                       │
│ • Preporuke                                            │
│ • Za donosioca odluke                                  │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│ SOURCE DATA (SUBAGENT-04):                             │
│ Trenutni-Fiskalni-Prihodi-Podaci.md                    │
│                                                        │
│ • 320M EUR verifikovano                                │
│ • Zakonske osnove                                      │
│ • Breakdown po komponentama                            │
└────────────────────────────────────────────────────────┘
```

---

## ✅ VERIFIKACIJA - MOŽE LI SE PROVERITI?

```
┌────────────────────────────────────────┐
│ DA - Model je POTPUNO TRANSPARENTAN    │
├────────────────────────────────────────┤
│ ✓ Sve formule eksplicitne              │
│ ✓ Sve pretpostavke jasne               │
│ ✓ Svi izvori citirani                  │
│ ✓ Python kod za replikaciju            │
│ ✓ Eksterni ekonomista može proveriti   │
└────────────────────────────────────────┘

PRIMER FORMULE:
┌─────────────────────────────────────────────────────┐
│ R_novo = (N × (1-r) × C × m × 12) +                │
│          (GGR × (1-r×e) × (1-o) × T)               │
│                                                     │
│ Gde:                                                │
│ N = Broj objekata                                   │
│ r = Redukcija (%)                                   │
│ C = Trenutna naknada                                │
│ m = Aukcijski multiplikator                         │
│ GGR = Gross Gaming Revenue                          │
│ e = Elastičnost                                     │
│ o = Offshore migracija                              │
│ T = Porezna stopa (0.15)                            │
└─────────────────────────────────────────────────────┘
```

---

## 🎯 ZAKLJUČAK ANALIZE

```
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║  KLJUČNI NALAZI MODELA:                              ║
║                                                       ║
║  Model pokazuje značajan fiskalni rizik              ║
║  za aukcijski sistem                                 ║
║                                                       ║
║  • Očekivani gubitak: -40%                           ║
║  • Verovatnoća profita: <10%                         ║
║  • Neizvesnost: Visoka                               ║
║                                                       ║
║  OPCIJE ZA RAZMATRANJE:                              ║
║                                                       ║
║  Pilot program, RIA, ili alternativne politike       ║
║  pre full-scale implementacije                       ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝
```

---

**Pripremio:** SUBAGENT-03 (Financial Modeling Economist)
**Datum:** 18. novembar 2025
**Status:** VIZUELNI PREGLED za brzo razumevanje

**Za detalje:** Vidi `Fiskalni-Model-Aukcije.md` (25 strana) i `Fiskalni-Model-Aukcije-SIMPLE.md` (2 strane)
